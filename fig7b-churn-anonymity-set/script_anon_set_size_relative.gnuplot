set terminal postscript eps size 3.5,2.62 enhanced color font 'Helvetica,21' linewidth 2
set output 'graph_anon_set_size_relative.eps'

set border linewidth 1
set style line 1 linecolor rgb '#0000FF' linetype 1 linewidth 2
set style line 2 linecolor rgb '#FF0000' linetype 2 linewidth 2
set style line 3 linecolor rgb '#8A2BE2' linetype 3 linewidth 2
set style line 4 linecolor rgb '#FFA500' linetype 3 linewidth 2
set style line 5 linecolor rgb '#800080' linetype 5 linewidth 3
set style line 6 linecolor rgb '#1E90FF' linetype 6 linewidth 3

set style fill solid

set nologscale y
set nologscale x

set key bottom right

set xrange [0:4]
set yrange [87:108]

set grid xtics  # draw lines for each ytics and mytics
set grid ytics  # draw lines for each ytics and mytics
set grid               # enable the grid

set title ""
set xlabel "Time [h]" offset 0,0.5
set ylabel "Anonymity Set Size [%]" offset 1.7,0

plot "cafe_anonymity_set_size_relative.txt" using ($1/3600):4 notitle with linespoint ls 1
