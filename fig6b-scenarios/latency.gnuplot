#set terminal pdf size 3.5,2.62
set terminal postscript eps size 3.5,2.62 enhanced color font 'Helvetica,21' linewidth 2
set output 'scenarios.eps'

set border linewidth 1
set style line 1 linecolor rgb '#0000FF' linetype 1 linewidth 3
set style line 2 linecolor rgb '#FF0000' linetype 2 linewidth 3
set style line 3 linecolor rgb '#8A2BE2' linetype 0 linewidth 3
set style line 4 linecolor rgb '#3f007f' linetype 3 linewidth 3
set style line 5 linecolor rgb '#800080' linetype 5 linewidth 3
set style line 6 linecolor rgb '#1E90FF' linetype 6 linewidth 3

set logscale y
set nologscale x

set key top left

set grid ytics xtics  # draw lines for each ytics and mytics
set grid               # enable the grid

#set xrange [0:30]
set yrange [10:2000]


set title ""
set xlabel "Number of clients" offset 0,0.5
set ylabel "[ms]" offset 1.7,0

set datafile separator ","
set bars large

plot 'vpn.gnudata'   using 1:2:3 title "VPN scenario" with lp ls 2, \
    'vpn.gnudata'    using 1:2:3 notitle with errorbar ls 2 lw 1, \
    'generalsetting.gnudata'   using 1:2:3 title "Standard scenario" with lp ls 1, \
    'generalsetting.gnudata'    using 1:2:3 notitle with errorbar ls 1 lw 1, \
    'icrc.gnudata'              using 1:2:3 title "One local guard" with lp ls 4 dashtype 3, \
    'icrc.gnudata'              using 1:2:3 notitle with errorbar ls 4 lw 1, \
    'baseline.gnudata' using 1:2 notitle with lp ls 3, \
    'baseline-vpn.gnudata' using 1:2 notitle with lp ls 3
