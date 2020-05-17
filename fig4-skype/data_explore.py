#!/usr/bin/python3

# usage: cat individualpcaps_.gnudata | ./stats.py

import fileinput
from pprint import pprint
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys

def try_parse_int(s, base=10):
  try:
    return int(s, base)
  except ValueError:
    return None

if len(sys.argv) < 2:
    print("Argument 1 must be the features to extract")
    sys.exit(1)

filename = sys.argv[1]

nPackets = 0;
data = [];
with open(filename) as file:
    for line in file:
        s = int(line.replace(',','').strip())
        data.append(s)

plt.plot(data)
plt.xlabel('Latency');
plt.xlabel('Packets');
plt.title(filename);
plt.show();