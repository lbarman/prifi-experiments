set terminal postscript eps size 3.5,2.62 enhanced color font 'Helvetica,21' linewidth 2
set output 'skype_5p_lat.eps'

set style line 3 linecolor rgb '#8A2BE2' linetype 0 linewidth 3

#set border 2 front lt black linewidth 1.000 dashtype solid
set boxwidth 5 absolute
set style fill solid 0.6 border lt -1
set pointsize 0.5
set style data boxplot
set xtics  norangelimit 
set xtics border in scale 0,0 nomirror norotate  autojustify
set ytics border in scale 1,0.5 nomirror norotate  autojustify
set yrange [ 0.00000 : 200.000 ] noreverse nowriteback
set xrange [ 0.00000 : 100.0 ] noreverse nowriteback
DEBUG_TERM_HTIC = 100
DEBUG_TERM_VTIC = 100


set key top left

set grid ytics xtics  # draw lines for each ytics and mytics
set grid               # enable the grid

set xlabel "Number of clients" offset 0,0.5
set ylabel "[ms]" offset 1.7,0

set style boxplot nooutliers
set datafile separator ","

plot 'individualpcaps_skype_1_10.gnudata' using (10):1 title "Latency with PriFi" linecolor rgb "#0000FF", \
     'individualpcaps_skype_2_20.gnudata' using (20):1 notitle linecolor rgb "#0000FF", \
     'individualpcaps_skype_2_30.gnudata' using (30):1 notitle linecolor rgb "#0000FF", \
     'individualpcaps_skype_2_40.gnudata' using (40):1 notitle linecolor rgb "#0000FF", \
     'individualpcaps_skype_3_50.gnudata' using (50):1 notitle linecolor rgb "#0000FF", \
     'individualpcaps_skype_4_60.gnudata' using (60):1 notitle linecolor rgb "#0000FF", \
     'individualpcaps_skype_4_70.gnudata' using (70):1 notitle linecolor rgb "#0000FF", \
     'individualpcaps_skype_4_80.gnudata' using (80):1 notitle linecolor rgb "#0000FF", \
     'individualpcaps_skype_5_90.gnudata' using (90):1 notitle linecolor rgb "#0000FF", \
     'baseline.gnudata' using 1:2 title "Baseline" with lp ls 3
     
