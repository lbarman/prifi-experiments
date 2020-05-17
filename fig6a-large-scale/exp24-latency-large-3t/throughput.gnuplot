#set terminal pdf size 3.5,2.62
set terminal postscript eps size 3.5,2.62 enhanced color font 'Helvetica,21' linewidth 2
set output 'throughput.eps'

set border linewidth 1
set style line 1 linecolor rgb '#0000FF' linetype 1 linewidth 3
set style line 2 linecolor rgb '#FF0000' linetype 2 linewidth 3
set style line 3 linecolor rgb '#8A2BE2' linetype 3 linewidth 3
set style line 4 linecolor rgb '#FFA500' linetype 4 linewidth 3
set style line 5 linecolor rgb '#800080' linetype 5 linewidth 3
set style line 6 linecolor rgb '#1E90FF' linetype 6 linewidth 3

set nologscale y
set nologscale x

set key top left

set grid ytics xtics  # draw lines for each ytics and mytics
set grid               # enable the grid

#set xrange [0:30]
#set yrange [0:15]

set title "Throughput"
set xlabel "Cellsize (up)" offset 0,0.5
set ylabel "[kbps]" offset 1.7,0

set datafile separator ","
set bars large

plot 'bw-up.gnudata' using 1:2:3 title "Upstream" with lp ls 1, \
    'bw-up.gnudata' using 1:2:3 notitle with errorbar ls 1 lw 1, \
    'bw-down.gnudata' using 1:2:3 title "Downstream" with lp ls 2, \
    'bw-down.gnudata' using 1:2:3 notitle with errorbar ls 2 lw 1, \
    'bw-down-udp.gnudata' using 1:2:3 title "Downstream (UDP)" with lp ls 3, \
    'bw-down-udp.gnudata' using 1:2:3 notitle with errorbar ls 3 lw 1,