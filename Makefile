.PHONY: all

all: chapter

%: 
	pdflatex --shell-escape $@.tex
	bibtex $@
	pdflatex --shell-escape $@.tex
	pdflatex --shell-escape $@.tex
