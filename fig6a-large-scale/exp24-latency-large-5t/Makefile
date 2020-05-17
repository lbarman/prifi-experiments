parse:
	../raw-to-json.sh

extract:
	rm -f *.compiled
	../fetch-info.py measured-latency > measured-latency.compiled
	../fetch-info.py stayed-in > stayed-in-buffer.compiled
	../fetch-info.py round-duration > round-duration.compiled
	../fetch-info.py waiting-on-clients > waiting-on-clients.compiled
	../fetch-info.py waiting-on-trustees > waiting-on-trustees.compiled
	../fetch-info.py sending-data > sending-data.compiled
	../fetch-info.py round_s > throughput.compiled
	../remove-empty.sh .compiled

aggregate:
	rm -f *.gnudata
	node ../aggregate.js round-duration.compiled ../aggregate-scripts/duration-mean-stable.js > round-duration.gnudata
	node ../aggregate.js measured-latency.compiled ../aggregate-scripts/duration-mean-stable.js > measured-latency.gnudata
	node ../aggregate.js stayed-in-buffer.compiled ../aggregate-scripts/duration-mean-stable.js > stayed-in-buffer.gnudata
	node ../aggregate.js waiting-on-clients.compiled ../aggregate-scripts/duration-mean-stable.js > waiting-on-clients.gnudata
	node ../aggregate.js waiting-on-trustees.compiled ../aggregate-scripts/duration-mean-stable.js > waiting-on-trustees.gnudata
	node ../aggregate.js sending-data.compiled ../aggregate-scripts/duration-mean-stable.js > sending-data.gnudata
	node ../aggregate.js throughput.compiled ../aggregate-scripts/round-sec.js > round-sec.gnudata
	node ../aggregate.js throughput.compiled ../aggregate-scripts/bw-up.js > bw-up.gnudata
	node ../aggregate.js throughput.compiled ../aggregate-scripts/bw-down.js > bw-down.gnudata
	node ../aggregate.js throughput.compiled ../aggregate-scripts/bw-down-udp.js > bw-down-udp.gnudata
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
	# rm -f *.gnudata
	rm -f *.eps

all: parse extract aggregate eps pdf clean
