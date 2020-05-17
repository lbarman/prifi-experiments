#set terminal pdf size 3.5,2.62
set terminal postscript eps size 3.5,2.62 enhanced color font 'Helvetica,21' linewidth 2
set output 'cpu.eps'

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

#set xrange [1:105]
#set yrange [1000:1800]

set title "CPU Usage - Anonymize"
set xlabel "Number of clients" offset 0,0.5
set ylabel "Mean CPU Usage [%]" offset 1.7,0

set datafile separator ","
set bars large

plot 'cpu.gnudata' using 1:2:3 notitle with lp ls 1, \
     'cpu.gnudata' using 1:2:3 notitle with errorbar ls 1 lw 1
