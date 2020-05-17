eps:
	rm -f *.eps
	for file in *.gnuplot ; do \
	    gnuplot $$file ; \
	done

pdf:
	rm -f *.pdf
	../epstopdfs.sh

plots: eps pdf

all: eps pdf
