#!/usr/bin/env python3
"""从源文件中的 %! 元数据生成页码对应索引。

约定：一个 %! 记录对应一张 frame，也对应最终 PDF 的一页；
封面 frame 记录在 main.tex 中。生成前会用 pdfinfo 校验页数。
"""
from __future__ import annotations
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "main.tex"
SECTIONS = [
    ROOT / "sections/00_front.tex",
    ROOT / "sections/01_energy.tex",
    ROOT / "sections/02_boiler.tex",
    ROOT / "sections/03_turbine.tex",
    ROOT / "sections/04_gasturbine.tex",
    ROOT / "sections/05_ice.tex",
    ROOT / "sections/06_close.tex",
]
META_RE = re.compile(r"^%!\s+src=(\d+)\s+kind=(\w+)\s+title=(.*)$")
SECTION_RE = re.compile(r"^\\section\{(.+?)\}")


def parse_records():
    records = []
    # 封面：main.tex 中唯一一条 src=0 kind=cover
    text = MAIN.read_text(encoding="utf-8")
    for line in text.splitlines():
        m = META_RE.match(line.strip())
        if m and m.group(2) == "cover":
            records.append({
                "page": len(records) + 1,
                "src": int(m.group(1)),
                "kind": "cover",
                "title": m.group(3).strip(),
                "section": "封面",
            })
            break
    if not records:
        raise SystemExit("main.tex 中未找到封面 %! 记录")

    current_section = "课程导读"
    for path in SECTIONS:
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            sm = SECTION_RE.match(line)
            if sm:
                current_section = sm.group(1)
                continue
            m = META_RE.match(line)
            if not m:
                continue
            records.append({
                "page": len(records) + 1,
                "src": int(m.group(1)),
                "kind": m.group(2),
                "title": m.group(3).strip(),
                "section": current_section,
            })
    return records


def pdf_pages():
    out = subprocess.check_output(["pdfinfo", str(ROOT / "main.pdf")], text=True)
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    raise SystemExit("pdfinfo 未返回 Pages")


def main():
    records = parse_records()
    n_pdf = pdf_pages()
    if len(records) != n_pdf:
        raise SystemExit(f"元数据 {len(records)} 条，PDF {n_pdf} 页，不一致")
    orig = [r for r in records if r["kind"] == "orig"]
    supp = [r for r in records if r["kind"] == "supp"]
    if [r["src"] for r in orig] != list(range(1, 73)):
        raise SystemExit("原页记录不是完整且有序的 1..72")
    if len(records) != 1 + 1 + 72 + len(supp):
        raise SystemExit("记录数不满足 1 封面 + 1 地图 + 72 原页 + 补充页")

    # TSV
    tsv = ["新PDF页\t原PDF页\t类型\t章节\t标题"]
    for r in records:
        tsv.append(f'{r["page"]}\t{r["src"]}\t{r["kind"]}\t{r["section"]}\t{r["title"]}')
    (ROOT / "slide-index.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
    (ROOT / "slide-index.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # 原页 -> 新页
    by_src = {}
    for r in records:
        if r["kind"] in {"orig", "supp"}:
            by_src.setdefault(r["src"], []).append(r)
    orig_rows = []
    for p in range(1, 73):
        rs = by_src[p]
        orig_rec = next(r for r in rs if r["kind"] == "orig")
        pages = "、".join(str(r["page"]) for r in rs)
        supp_pages = "、".join(str(r["page"]) for r in rs if r["kind"] == "supp") or "—"
        topic = orig_rec["title"].replace(f"原第 {p} 页｜", "").replace(f"原第{p}页｜", "")
        orig_rows.append((p, pages, supp_pages, orig_rec["section"], topic))

    type_name = {"cover": "封面", "nav": "课程地图", "orig": "原页总结", "supp": "补充"}
    new_rows = [(r["page"], r["src"], type_name[r["kind"]], r["section"], r["title"]) for r in records]

    md = []
    md.append("# 原 PDF 页码 — 新 PDF 页码对应表\n")
    md.append("本表由 `tools/build_index.py` 从各内容文件的 `%!` 元数据自动生成，")
    md.append("并与最终 PDF 页数、原页 1–72 的覆盖情况做了校验。\n")
    md.append(f"- 新 PDF 总页数：**{len(records)}**")
    md.append("- 原页总结：**72** 页（原第 1–72 页，每页至少一张）")
    md.append(f"- 补充页：**{len(supp)}** 页")
    md.append("- 另有封面 1 页、课程地图 1 页\n")
    md.append("## 按原页查找\n")
    md.append("| 原 PDF 页 | 新 PDF 页 | 其中补充页 | 单元 | 主题 |")
    md.append("|---:|---|---|---|---|")
    for p, pages, supp_pages, section, topic in orig_rows:
        md.append(f"| {p} | {pages} | {supp_pages} | {section} | {topic} |")
    md.append("\n## 按新 PDF 页查找\n")
    md.append("| 新 PDF 页 | 原 PDF 页 | 类型 | 单元 | 标题 |")
    md.append("|---:|---:|---|---|---|")
    for page, src, typ, section, title in new_rows:
        src_text = "—" if src == 0 else str(src)
        md.append(f"| {page} | {src_text} | {typ} | {section} | {title} |")
    md.append("\n## 说明\n")
    md.append("- 标题中的“原第 \\(XX\\) 页”指原课件《期中总结.pdf》的物理页码。")
    md.append("- 一个原页可以对应多页：原页总结 + 若干补充页。")
    md.append("- 封面、课程地图不对应原页；原第 1 页是课件封面，本整理用作阅读说明。")
    md.append("- 若重新增删 frame，请重新运行 `python3 tools/build_index.py`，并确认 PDF 页数同步变化。")
    (ROOT / "页码对应表.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"OK: {len(records)} pages, 72 originals, {len(supp)} supplements")


if __name__ == "__main__":
    main()
