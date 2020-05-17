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
                    p1 = key[0:key.find("_")]
                    p2 = key[key.find("_")+1:]
                    try:
                        obj["_key"] = int(p1)
                    except:
                        obj["_key"] = p1
                    obj["_key2"] = int(p2)
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

outLines.sort(key=lambda x:x["_key"])

for line in outLines:
    print json.dumps(line, sort_keys=True)+","
