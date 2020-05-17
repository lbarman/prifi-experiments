parse:
	../raw-to-json.sh

extract:
	grep "PCAPLog-individuals" logs/* > pcap-individuals.grepped
	grep "(*BitrateStatistics).ReportWithInfo" logs/* > bitratestats.grepped
	python2 pcap-individuals.py pcap-individuals.grepped
	python2 bitratestats.py bitratestats.grepped

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
	# rm -f *.gnudata
	rm -f *.eps

all: parse extract eps pdf clean
