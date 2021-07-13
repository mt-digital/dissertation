build:
	python3 builder.py

first: 
	xelatex -shell-escape Thesis.tex

main: first
	bibtex Thesis && xelatex -shell-escape Thesis.tex

omain: main
	open Thesis.pdf

clean:
	rm -f *.aux Thesis.{log,out,blg,bbl,toc,lof,lot}
