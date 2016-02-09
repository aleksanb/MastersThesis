file = "main"
pdffile = ${file}".pdf"

.PHONY: all
all: build

.PHONY: guard
guard:
	MAIN_FILE=$(file) bundle exec guard

.PHONY: upload
upload:
	bash -i -c "upload $(pdffile)"

.PHONY: open
open:
	evince $(pdffile) &

.PHONY: clean
clean:
	rm -f *.aux *.bbl *.blg *.xml *.log *blx.bib *blg *blg *.tdo *.glo *.lof *.lot *.out *toc
