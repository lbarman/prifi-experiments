FIGURE_DIRS=$(wildcard fig*/)

install:
	npm install -G underscore
	#node JS, python3, gnuplot, epstopdf

rebuild: $(FIGURE_DIRS)

$(FIGURE_DIRS):
	$(MAKE) -C $@ all

.PHONY: rebuild $(FIGURE_DIRS)