parse:
	../raw-to-json.sh

extract:
	rm -f *.compiled
	../fetch-info.py measured-latency > measured-latency.compiled
	../remove-empty.sh .compiled

aggregate:
	rm -f *.gnudata
	node ../aggregate.js measured-latency.compiled ../aggregate-scripts/duration-mean-stable.js > measured-latency.gnudata
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
