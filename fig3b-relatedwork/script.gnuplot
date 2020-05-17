#set terminal pdf size 3.5,2.62
set terminal postscript eps size 3.5,2.62 enhanced color font 'Helvetica,21' linewidth 2
set output 'prifi-dissent.eps'

set border linewidth 1
set style line 1 linecolor rgb '#0000FF' linetype 1 linewidth 3
set style line 2 linecolor rgb '#FF0000' linetype 2 linewidth 3
set style line 3 linecolor rgb '#8A2BE2' linetype 0 linewidth 3
set style line 4 linecolor rgb '#FFA500' linetype 4 linewidth 3
set style line 5 linecolor rgb '#800080' linetype 5 linewidth 3
set style line 6 linecolor rgb '#1E90FF' linetype 6 linewidth 3

set logscale y
set nologscale x

set key top right

set grid ytics xtics  # draw lines for each ytics and mytics
set grid               # enable the grid

#set xrange [0:30]
set yrange [0.005:5000]

set title ""
set xlabel "Number of clients" offset 0,0.5
set ylabel "[s]" offset 1.7,0

set datafile separator ","
set bars large

plot 'dissent.gnudata' using 1:($2/1000):($3/1000) title "Dissent in Numbers (D#)" with lp ls 2 dashtype 3, \
    'dissent.gnudata' using 1:($2/1000):($3/1000) notitle with errorbar ls 2 lw 1, \
    'riffle.gnudata' using 1:($2/1000):($3/1000) title "Riffle (Microblogging)" with lp ls 4, \
    'riffle.gnudata' using 1:($2/1000):($3/1000) notitle with errorbar ls 4 lw 1, \
    'prifi.gnudata' using 1:($2/1000):($3/1000) title "PriFi" with lp ls 1, \
    'prifi.gnudata' using 1:($2/1000):($3/1000) notitle with errorbar ls 1 lw 1, \
    'baseline.gnudata' using 1:($2/1000) title "Baseline" with lp ls 3
