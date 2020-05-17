eps:
	rm -f *.eps
	../gnuplots.sh

pdf:
	rm -f *.pdf
	../epstopdfs.sh

plots: eps pdf

clean:
	# rm -f *.gnudata

all: eps pdf clean
