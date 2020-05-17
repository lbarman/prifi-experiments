#!/usr/bin/python3

# usage: cat individualpcaps_.gnudata | ./stats.py

from pathlib import Path
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def try_parse_int(s, base=10):
  try:
    return int(s, base)
  except ValueError:
    return None

def processPoint(fileScheme):
    plotData = {}

    pathlist = Path("logs").glob(fileScheme)
    for path in pathlist:
        filename = str(path)
        with open(filename) as file:
            fileData = []
            for line in file:
                needle = "PCAPLog-individuals "
                if needle in line:
                    line = line[line.find(needle) + len(needle):].replace('( ', '').replace(' )', '').strip()
                    parts = line.split(':')
                    key = parts[0].strip()
                    data = parts[1].strip().split(';')
                    print(data)
                    data = [try_parse_int(x) for x in data if x != ""]
                    #fileData[key] = data
                    fileData.extend(data)
        plotData[filename] = fileData
        plt.plot(fileData, label=filename)

    plt.ylabel('Latency');
    plt.xlabel('Packets');
    plt.title(fileScheme);
    plt.legend(loc='best')
    plt.show();

processPoint('experiment_skype.pcap_10_1_*.txt')
processPoint('experiment_skype.pcap_20_1_*.txt')
processPoint('experiment_skype.pcap_30_1_*.txt')
#processPoint('experiment_skype.pcap_50_1_*.txt')
#processPoint('experiment_skype.pcap_70_1_*.txt')
#processPoint('experiment_skype.pcap_90_1_*.txt')
