import sys
import re
import json
import collections

regex1str = "{\"pcap_time_diff\": \"([-\d]+)\""
regex1 = re.compile(regex1str)

json = []

pcapsNames = []
payloads = []

def is_number(s):
    try:
        float(s)
        if float(s) > 10:
            return True
        return False
    except ValueError:
        return False

def parseGreppedToObject(inFile):
    data = []
    with open(inFile) as file:
        rawData = file.read()
        lines = rawData.split("\n")

        # parse the data
        for line in lines:
            if line.strip() == "":
                continue

            lineout = {}

            line = line.replace('.txt:[0m[0;33m1 : (                                    utils.(*PCAPLog).Print: 125) - PCAPLog-individuals (', '').replace(' ):  ', ' ');
            parts = line.split(' ');
            filename = parts[0];
            if "logs/" in filename:
                filename = filename.replace('logs/', '')
            filename.strip()
            client = parts[-3].strip()
            data = parts[-1].strip()

            filenamedata = filename.split('_')
            lineout['pcap'] = filenamedata[0].replace('.pcap', '')
            lineout['payload'] = filenamedata[1]
            lineout['repeat'] = filenamedata[2]
            lineout['data'] = data.split(';')
            lineout['client'] = client

            json.append(lineout)

            if lineout['pcap'] not in pcapsNames:
                pcapsNames.append(lineout['pcap'])
            if lineout['payload'] not in payloads:
                payloads.append(lineout['payload'])
            #print lineout

if len(sys.argv) < 2:
    print "Argument 1 must be the input file"
    sys.exit(1)

a = str(sys.argv[1])
parseGreppedToObject(a)

for pcap in pcapsNames:
    mergedData = {}

    for line in json:
        if line['pcap'] == pcap:

            if not line['payload'] in mergedData:
                mergedData[line['payload']] = []


            mergedData[line['payload']].extend(filter(is_number, line['data']))


    od = collections.OrderedDict(sorted(mergedData.items()))

    for payload, data in od.items():
        with open("individualpcaps_"+pcap+"_"+payload+".gnudata", "w") as file:
            for v in data:
                file.write(v+",\n")