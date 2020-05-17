set terminal postscript eps size 3.5,2.62 enhanced color font 'Helvetica,21' linewidth 2
set output 'skype_5p_bw.eps'

set xtics border in scale 0,0 nomirror norotate  autojustify
set ytics border in scale 1,0.5 nomirror norotate  autojustify
DEBUG_TERM_HTIC = 100
DEBUG_TERM_VTIC = 100

set grid ytics xtics  # draw lines for each ytics and mytics
set grid               # enable the grid

set xlabel "Number of clients" offset 0,0.5
set ylabel "[Mbps]" offset 1.7,0

set style fill solid 0.6 border lt -1

set style data histogram 
set style histogram rowstacked errorbars gap 1 lw 1
set boxwidth 1 relative
set style fill solid 1.0 border -1
#set style histogram cluster gap 1
#set style fill solid border -1
#set boxwidth 0.9
#set xtic scale 0
set auto x

set yrange [0.1:400]

set logscale y

set datafile separator ","

plot 'bitratestats_skype.gnudata' using ($6):($7):xtic(1) title "Payload" linecolor rgb "#0000FF", \
    'bitratestats_skype.gnudata' using ($3/1024):($5/1024):xtic(1) fs pattern 2 title "PriFi LAN Traffic" linecolor rgb "#0000FF", \
    'bitratestats_skype.gnudata' using (3*$2/1024):($4/1024):xtic(1) fs pattern 4 title "PriFi WAN Traffic" linecolor rgb "#FF0000"
