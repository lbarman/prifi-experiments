#!/usr/bin/python2

import os
import sys
import json

data = []

if len(sys.argv) < 2:
    print "Argument 1 must be the features to extract"
    sys.exit(1)

feature = sys.argv[1]

outLines = []

def processFile(inFile):
    global logFolder
    data = []
    with open(logFolder + inFile) as file:
        rawData = file.read()
        rawData = rawData.replace("},\n]", "}]")
        j = json.loads(rawData)

        for obj in j:
            take=False
            for key in obj:
                if feature in key or feature in obj[key]:
                    take=True
            if take:
                key = inFile.replace("experiment_", "").replace(".json", "")
                if "_" in key :
                    parts = key.split("_")
                    p1 = int(parts[0])
                    p2 = int(parts[1])
                    repeat = int(parts[2])
                    obj["_key2"] = int(p1)
                    obj["_key"] = int(p2)
                    obj["_repeat"] = int(repeat)
                else:
                    obj["_key"] = int(key)
                outLines.append(obj)



logFolder = "logs/"
# list all files in dir
files = []
for (dirpath, dirnames, filenames) in os.walk(logFolder):
    files = filenames
    break

for file in files:
    if ".json" not in file:
        continue
    processFile(file)

outLines.sort(key=lambda x: (x["_key"], x["_key2"]))

for line in outLines:
    print json.dumps(line, sort_keys=True)+","
