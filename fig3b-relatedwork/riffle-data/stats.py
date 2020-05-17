import os
import sys
from os import listdir
import numpy as np
from os.path import isfile, join
files = [f for f in listdir('.') if isfile(f) and '.txt' in f and 'out_' in f]
files.sort()

stats = dict()

for file in files:
    with open(file) as f:
        content = f.read()
        lines = content.split('\n')
        
        fname = file.replace('out_', '').replace('.txt', '').split('_')

        if len(fname) != 2:
            print("Weird name:", fname)
            sys.exit(1)
        
        nclients = int(fname[0])
        repeat = fname[1]
        sharingkeys = lines[0].replace('sharing keys  took  ', '').replace('s', '')
        totaltime = lines[2].replace('total time:  took  ', '').replace('s', '')
        
        if not nclients in stats:
            stats[nclients] = []
        stats[nclients].append([sharingkeys, totaltime])

def mean(arr):
    acc = 0
    for v in arr:
        acc += float(v)
    return float(acc)/len(arr)

nclients = list(stats.keys())
nclients.sort()

with open("riffle.txt", "w") as f:
    for nclient in nclients:
        totaltimes = [1000*float(x[1]) for x in stats[nclient]] # go to ms
        setuptimes = [1000*float(x[0]) for x in stats[nclient]] # go to ms
        m = round(mean(totaltimes))
        dev = round(np.std(totaltimes))
        print(nclient, m, dev, round(mean(setuptimes)), round(np.std(setuptimes)))
        f.write(str(nclient) + ",\t" + str(m) + ",\t" + str(dev) +"\n")
