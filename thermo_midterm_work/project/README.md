# 热能动力工程 · 期中总结（SJTUBeamer 扩充版）

本工程把《期中总结.pdf》72 页课件整理为逐页对应、带补充推导和读图说明的 SJTUBeamer 幻灯片。正文 PDF 共 **103 页**：封面 1 页、课程地图 1 页、原页总结 72 页、补充 29 页。

- 模板：SJTUBeamer 3.1.0，使用 `min,red,light,infolines,topright` 主题选项；已完整复制模板并在副本上修改，原模板目录未改动。
- 文档类：`ctexbeamer`，16:9；中文字体使用 TeX Live 自带的 Fandol，XeLaTeX 编译。
- 页码：页脚右侧为 `当前页/总页数`；每页标题以“原第 XX 页”或“原第 XX 页补充”开头。
- 索引：`页码对应表.md`、`slide-index.tsv`、`slide-index.json`，由 `tools/build_index.py` 从源文件元数据生成并校验。

## 快速编译

在工程根目录执行：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

或：

```bash
make
```

生成 `main.pdf`。`latexmk` 会自动处理多次编译与 `\inserttotalframenumber` 的总页数。清理辅助文件：

```bash
make clean
```

更详细的环境、字体与排错说明见 [编译说明.md](编译说明.md)。

## 目录结构

```text
.
├── main.tex                 # 主文件（封面、章节输入、PDF 元数据）
├── styles.tex               # 版式、颜色、tcolorbox、TikZ 样式
├── sections/
│   ├── 00_front.tex         # 原第 1 页、课程地图
│   ├── 01_energy.tex        # 原第 2–7 页
│   ├── 02_boiler.tex        # 原第 8–24 页
│   ├── 03_turbine.tex       # 原第 25–46 页
│   ├── 04_gasturbine.tex    # 原第 47–59 页
│   ├── 05_ice.tex           # 原第 60–72 页
│   └── 06_close.tex         # 预留（当前为空）
├── figures/course/          # 由原课件裁切并检查过的结构/循环图
│   ├── engine_structure.png
│   ├── four_stroke.png
│   └── two_stroke.png
├── vi/                      # SJTUBeamer 徽标、封面图等模板资源
├── *.sty                    # 主题文件（SJTUBeamer 3.1.0）
├── tools/
│   ├── build_index.py       # 生成页码索引并校验 72 页覆盖
│   └── verify.py            # 编译产物与索引一致性核验
├── slide-index.tsv          # 新页 ↔ 原页 ↔ 类型 ↔ 标题
├── slide-index.json         # 同上，机器可读
├── 页码对应表.md            # 原页查找 + 新页查找
├── 验证记录.md              # 实际编译、页数、缺字、越界等检查记录
├── reference/               # 原逐页 Markdown 备份与来源校验和
├── 编译说明.md
└── main.pdf                 # 已编译的 103 页 PDF
```

## 内容标识

- **原课件**：对应原页的定义、流程、公式、数值与课件比较结论。
- **补充**：物理含义、变量单位、必要推导、适用条件、易混点；不冒充课件原文。
- **阅读提示**：说明流程图、焓熵图、速度三角形、T–s 图、结构图的读图顺序。
- 经验数值标为“课件示例/课件值”，并在相应页说明适用范围；不把示例值泛化为所有机组参数。
- 对疑似笔误或条件不明处，采用“原页下标疑为……”“课件未给全单位”“这里按……理解”等表述，未静默改写成确定结论。主要包括：
  - 原第 30 页将轮周比功表述为“单位质量蒸汽在单位时间内所做的功”；
  - 原第 31 页 \(2t'\) 的投影/下标易混，\(\Delta h_t\approx\Delta h_n+\Delta h_b\) 是近似式；
  - 原第 43 页经济真空图纵轴旁写了 \(p_c\)，但曲线实际是 \(N_{el}\) 与 \(P_{pump}\)；
  - 原第 58 页用 \(P_{gt}\) 表示量纲为比功的式子；
  - 原第 59 页涡轮效率分母的 \(4s1\) 疑为 \(4s\)；
  - 原第 24 页末条 \(q_6\approx0\) 判据在投影页上未给全单位；
  - 汽轮机章节 \(P_e\) 指轴功率，内燃机章节 \(P_e\) 指有效功率，本整理在跨章节处重新声明。

## 索引与重建

新增、删除或移动 frame 后：

```bash
python3 tools/build_index.py
python3 tools/verify.py
```

`build_index.py` 会检查：PDF 页数与 `%!` 元数据条数一致、原页 1–72 完整且有序、补充页数量与索引一致。`verify.py` 会检查标题覆盖、缺字、日志越界、PDF 尺寸/页数等。

## 图片说明

- `figures/course/engine_structure.png`、`four_stroke.png`、`two_stroke.png` 来自原课件第 62、67、68 页的局部裁切，保留主要中文标注；裁切时已去除页眉、页脚和装饰边，检查过四冲程/二冲程标题与左右标注的完整性。
- 其余示意图（锅炉流程、自然循环、速度三角形、h–s 图、凝汽器、布雷顿 T–s 图、经济真空曲线、内燃机几何等）用 TikZ/pgfplots 重绘，图中标注与正文公式采用同一套符号。
- 所有示意图都不是按比例工程图；用于解释概念、方向和能量边界，具体设计尺寸以教材/设备资料为准。

## 验证摘要

在 macOS + TeX Live 2026 下完成最终编译；`pdfinfo` 显示 103 页、页面 453.54 × 255.12 pt（16:9）。最终日志无 `Overfull`、无缺字、无未定义引用；72 个原页标题全部可检索，29 个补充页与索引一致。逐页缩略图检查加重点页 200 dpi 全尺寸检查；未做 OCR 像素级比对。详细命令与结果见 [验证记录.md](验证记录.md)。

## 许可与用途

- SJTUBeamer 主题文件遵循其原 Apache-2.0 许可，见 `LICENSE`。
- 课件原图、课程文字与课程数据版权归原课程/原作者；本工程用于个人复习，不构成对原课件的再授权。
- 补充推导与排版为本整理新增内容；引用原课件数据时请保留“课件示例”限定。
