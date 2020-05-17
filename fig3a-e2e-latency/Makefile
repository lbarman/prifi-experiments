parse:
	../raw-to-json-old-format.sh

extract:
	rm -f *.compiled
	../fetch-info.py measured-latency > measured-latency.compiled
	../fetch-info.py stayed-in > stayed-in-buffer.compiled
	../remove-empty.sh .compiled

aggregate:
	node ../aggregate.js measured-latency.compiled ../aggregate-scripts/duration-mean.js > measured-latency.gnudata
	node ../aggregate.js stayed-in-buffer.compiled ../aggregate-scripts/duration-mean.js > stayed-in-buffer.gnudata
	../remove-empty.sh .gnudata

eps:
	rm -f *.eps
	../gnuplots.sh

pdf:
	rm -f *.pdf
	../epstopdfs.sh

plots: eps pdf

clean:
	rm -f logs/*.json
	rm -f *.compiled

all: parse extract aggregate eps pdf clean
