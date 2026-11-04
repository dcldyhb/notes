#!/usr/bin/env python3
"""对最终 PDF、编译日志和页码索引做一致性核验。"""
from __future__ import annotations
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "main.pdf"
LOG = ROOT / "main.log"
TSV = ROOT / "slide-index.tsv"


def run(cmd):
    return subprocess.check_output(cmd, cwd=ROOT, text=True) \
        if isinstance(cmd, list) else subprocess.check_output(cmd, cwd=ROOT, shell=True, text=True)


def main():
    problems = []

    info = run(["pdfinfo", str(PDF)])
    pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
    size = re.search(r"^Page size:\s+([\d.]+) x ([\d.]+) pts", info, re.M)
    w, h = float(size.group(1)), float(size.group(2))

    rows = []
    for line in TSV.read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) >= 5:
            rows.append(parts)
    if len(rows) != pages:
        problems.append(f"索引 {len(rows)} 行，PDF {pages} 页")
    if abs(w / h - 16 / 9) > 0.01:
        problems.append(f"页面比例不是 16:9: {w} x {h}")

    orig = [int(r[1]) for r in rows if r[2] == "orig"]
    supp = [r for r in rows if r[2] == "supp"]
    if orig != list(range(1, 73)):
        problems.append(f"原页记录不完整/无序: {orig}")

    text = run(["pdftotext", "-layout", str(PDF), "-"])
    missing = [n for n in range(1, 73) if not re.search(rf"原第\s*{n}\s*页", text)]
    if missing:
        problems.append(f"PDF 文本中缺少原页标题: {missing}")

    log_exists = LOG.exists()
    if log_exists:
        log = LOG.read_text(encoding="utf-8", errors="ignore")
    else:
        log = ""
        print("WARN: main.log 不存在，跳过日志中的 Overfull/缺字检查；请先执行 make 或 latexmk 以生成日志。")
    for pat, label in [
        (r"Overfull \\hbox", "Overfull hbox"),
        (r"Overfull \\vbox", "Overfull vbox"),
        (r"Missing character", "Missing character"),
        (r"Undefined control sequence", "Undefined control sequence"),
        (r"LaTeX Warning: There were undefined references", "undefined references"),
    ]:
        if log_exists and re.search(pat, log):
            problems.append(f"日志中发现: {label}")

    # 字体嵌入
    fonts = run(["pdffonts", str(PDF)])
    font_lines = [ln for ln in fonts.splitlines()[2:] if ln.strip()]
    not_embedded = []
    for ln in font_lines:
        m = re.search(r'\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+0$', ln)
        if m and m.group(1) != "yes":
            not_embedded.append(ln)
    if not_embedded:
        problems.append(f"有字体未嵌入: {len(not_embedded)}")

    # 文本 bbox 越界（容差 1.5 pt）
    bbox = run(["pdftotext", "-bbox", str(PDF), "-"])
    page_matches = list(re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">', bbox))
    if page_matches:
        for pm in page_matches:
            pw, ph = float(pm.group(1)), float(pm.group(2))
            pno = len(re.findall(r'<page ', bbox[:pm.start()])) + 1
            segment_end = bbox.find("</page>", pm.end())
            seg = bbox[pm.end():segment_end if segment_end > 0 else len(bbox)]
            for wm in re.finditer(r'xMin="([-\d.]+)" yMin="([-\d.]+)" xMax="([-\d.]+)" yMax="([-\d.]+)"', seg):
                xmin, ymin, xmax, ymax = map(float, wm.groups())
                if xmin < -1.5 or ymin < -1.5 or xmax > pw + 1.5 or ymax > ph + 1.5:
                    problems.append(f"第 {pno} 页文本越界: {xmin},{ymin},{xmax},{ymax} (page {pw}x{ph})")
                    break

    print(f"PDF: {pages} pages, {w:.2f} x {h:.2f} pt")
    print(f"索引: {len(rows)} 行, 原页 {len(orig)} 个, 补充 {len(supp)} 个")
    print(f"字体: {len(font_lines)} 个字体，未嵌入 {len(not_embedded)} 个")
    if problems:
        print("\nFAIL:")
        for p in problems:
            print("-", p)
        raise SystemExit(1)
    if log_exists:
        print("\nPASS: 页数、16:9、72 个原页、标题、日志、字体与文本边界检查通过。")
    else:
        print("\nPASS: 页数、16:9、72 个原页、标题、字体与文本边界检查通过（日志检查已跳过）。")


if __name__ == "__main__":
    main()
