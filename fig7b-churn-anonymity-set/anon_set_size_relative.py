#!/usr/bin/python3

import sys
import csv
import math
import numpy

MIN_DIFF = 0.1

assoc = []
disassoc = []

with open('cafe_association.csv', 'r') as csvfile:
    f = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in f:
        assoc.append(row)

with open('cafe_disassociation.csv', 'r') as csvfile:
    f = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in f:
        disassoc.append(row)

# print assoc
assocFiltered = []
lastIndexInOut = 0
assocFiltered.append((float(assoc[1][1]), assoc[1][2]))
i=2
while i<len(assoc):
    diff = float(assoc[i][1]) - assocFiltered[lastIndexInOut][0]
    if diff > MIN_DIFF:
        assocFiltered.append( (float(assoc[i][1]), assoc[i][2]) )
        lastIndexInOut += 1
    i+=1

# print disassoc
disassocFiltered = []
lastIndexInOut = 0
disassocFiltered.append((float(disassoc[1][1]), disassoc[1][2]))
i=2
while i<len(disassoc):
    diff = float(disassoc[i][1]) - disassocFiltered[lastIndexInOut][0]
    if diff > MIN_DIFF:
        disassocFiltered.append( (float(disassoc[i][1]), disassoc[i][2]) )
        lastIndexInOut += 1
    i+=1


# compute up-down time
bothFiltered = []
for a in assocFiltered:
    bothFiltered.append((a[0], a[1], 'a'))
for a in disassocFiltered:
    bothFiltered.append((a[0], a[1], 'd'))
bothFiltered = sorted(bothFiltered)

anonSet = [ '40:d6:43:bb:3d:c7' ] #this one device was already there, but disconnects at some point

# from _first10min.pcap
anonSet.append("00:0f:34:bd:4f:0c")
anonSet.append("00:16:6f:4d:0d:10")
anonSet.append("00:07:e9:86:11:c0")
anonSet.append("00:13:ce:aa:71:9b")
anonSet.append("00:13:ce:b1:94:84")
anonSet.append("00:11:24:86:30:d6")
anonSet.append("00:13:ce:67:a1:16")
anonSet.append("00:90:96:36:4b:a5")
anonSet.append("00:15:00:5d:a1:0c")
anonSet.append("00:11:24:fe:1c:7b")
anonSet.append("00:0e:9b:e2:68:ee")
anonSet.append("00:12:f0:10:1b:6d")
anonSet.append("00:14:a5:13:4e:83")
anonSet.append("00:0b:7d:ac:e9:bc")
anonSet.append("00:16:ce:1f:e1:f0")
anonSet.append("00:10:c6:3b:78:36")
anonSet.append("00:16:6f:34:f7:25")
anonSet.append("00:0f:f7:14:77:76")
anonSet.append("00:14:6c:f5:52:2b")
anonSet.append("00:90:4b:b6:6e:b1")
anonSet.append("00:90:4b:c8:cc:d4")
anonSet.append("00:11:85:17:ce:4c")
anonSet.append("00:16:6f:a4:5d:36")
anonSet.append("00:0f:34:64:23:ec")
anonSet.append("3c:da:92:6f:ce:f3")
anonSet.append("ff:ff:df:ed:ff:ff")
anonSet.append("ff:ff:ff:fd:ce:fe")
anonSet.append("01:00:0c:c1:a5:2d")
anonSet.append("00:0d:0b:5a:f6:3e")
anonSet.append("00:13:46:4d:85:68")
anonSet.append("00:16:b6:c9:67:b5")
anonSet.append("01:00:5e:e3:29:4f")
anonSet.append("00:12:f0:f4:82:e5")
anonSet.append("00:11:f5:6e:fa:bd")
anonSet.append("00:0c:41:42:eb:a9")
anonSet.append("00:14:a4:02:6d:3a")
anonSet.append("00:90:96:65:f4:fc")
anonSet.append("00:15:00:7b:f5:fb")
anonSet.append("00:11:24:40:20:07")


x=[]
y=[]

#print
anonSetOverTime = []
for e in bothFiltered:
    if e[2] == 'a':
        anonSet.append(e[1])
    else:
        if e[1] not in anonSet:
            print(e[1], "Disconnected twice, ignoring")
        else:
            anonSet.remove(e[1])
    anonSet = list(set(anonSet))
    #print(e[0], len(anonSet))

    x.append(e[0])
    y.append(len(anonSet))

#find regression with numpy
regression = numpy.polyfit(x, y, 1)


f = open('cafe_anonymity_set_size_reg.txt', 'w')
f.write("%s   %s\n" % (0, float(regression[1])))
f.write("%s   %s\n" % (14400, float(14400*regression[0]+regression[1])))
f.close()

x=[]
y=[]


anonSet = [ '40:d6:43:bb:3d:c7' ] #this one device was already there, but disconnects at some point

# from _first10min.pcap
anonSet.append("00:0f:34:bd:4f:0c")
anonSet.append("00:16:6f:4d:0d:10")
anonSet.append("00:07:e9:86:11:c0")
anonSet.append("00:13:ce:aa:71:9b")
anonSet.append("00:13:ce:b1:94:84")
anonSet.append("00:11:24:86:30:d6")
anonSet.append("00:13:ce:67:a1:16")
anonSet.append("00:90:96:36:4b:a5")
anonSet.append("00:15:00:5d:a1:0c")
anonSet.append("00:11:24:fe:1c:7b")
anonSet.append("00:0e:9b:e2:68:ee")
anonSet.append("00:12:f0:10:1b:6d")
anonSet.append("00:14:a5:13:4e:83")
anonSet.append("00:0b:7d:ac:e9:bc")
anonSet.append("00:16:ce:1f:e1:f0")
anonSet.append("00:10:c6:3b:78:36")
anonSet.append("00:16:6f:34:f7:25")
anonSet.append("00:0f:f7:14:77:76")
anonSet.append("00:14:6c:f5:52:2b")
anonSet.append("00:90:4b:b6:6e:b1")
anonSet.append("00:90:4b:c8:cc:d4")
anonSet.append("00:11:85:17:ce:4c")
anonSet.append("00:16:6f:a4:5d:36")
anonSet.append("00:0f:34:64:23:ec")
anonSet.append("3c:da:92:6f:ce:f3")
anonSet.append("ff:ff:df:ed:ff:ff")
anonSet.append("ff:ff:ff:fd:ce:fe")
anonSet.append("01:00:0c:c1:a5:2d")
anonSet.append("00:0d:0b:5a:f6:3e")
anonSet.append("00:13:46:4d:85:68")
anonSet.append("00:16:b6:c9:67:b5")
anonSet.append("01:00:5e:e3:29:4f")
anonSet.append("00:12:f0:f4:82:e5")
anonSet.append("00:11:f5:6e:fa:bd")
anonSet.append("00:0c:41:42:eb:a9")
anonSet.append("00:14:a4:02:6d:3a")
anonSet.append("00:90:96:65:f4:fc")
anonSet.append("00:15:00:7b:f5:fb")
anonSet.append("00:11:24:40:20:07")

#print
f = open('cafe_anonymity_set_size_relative.txt', 'w')
anonSetOverTime = []

differenceWith100 = None

for e in bothFiltered:
    time, mac = e[0], e[1]
    association = (e[2] == 'a')

    if association:
        anonSet.append(mac)
    else:
        if mac not in anonSet:
            print(mac, "Disconnected twice, ignoring")
        else:
            anonSet.remove(mac)
    anonSet = list(set(anonSet))
    newSize = len(anonSet)

    # remove linear trend
    regressionPoint = float(time)*regression[0] + regression[1]

    # remove origin diff
    if differenceWith100 is None:
        differenceWith100 = 100 - newSize/regressionPoint * 100


    diff = newSize/regressionPoint * 100 + differenceWith100

    f.write("%s   %s    %s    %s\n" % (e[0], regressionPoint, newSize, diff))

f.close()