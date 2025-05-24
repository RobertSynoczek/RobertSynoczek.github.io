# Makefile

INDEX_HTML := index.html

.PHONY: gen_site

gen_site:
	# Generate cosmoscope
	cosma m
	# Rename output
	mv cosmoscope.html $(INDEX_HTML)
	# Add KaTeX snippet
	python3 add_katex.py -f $(INDEX_HTML)