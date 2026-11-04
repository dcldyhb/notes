# 热能动力工程·期中总结（SJTUBeamer 扩充版）
LATEXMK ?= latexmk
LATEXMK_FLAGS = -xelatex -interaction=nonstopmode -halt-on-error

.PHONY: all pdf index verify clean

all: pdf

pdf: main.pdf

main.pdf: main.tex styles.tex $(wildcard sections/*.tex) $(wildcard figures/course/*)
	$(LATEXMK) $(LATEXMK_FLAGS) main.tex

index:
	python3 tools/build_index.py

verify: pdf index
	python3 tools/verify.py

clean:
	$(LATEXMK) -C main.tex
