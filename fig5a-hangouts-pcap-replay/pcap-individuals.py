import sys
import re
import json
import collections

regex1str = "{\"pcap_time_diff\": \"([-\d]+)\""
regex1 = re.compile(regex1str)

json = []

pcapsNames = []
nClientsVals = []
nActiveClientsVals = []

def is_number(s):
    try:
        float(s)
        return True
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

            line = line.replace('.txt:[0m[0;33m1 : (                                    utils.(*PCAPLog).Print: 117) - PCAPLog-individuals (', '').replace(' ):  ', ' ');
            parts = line.split(' ');
            filename = parts[0];
            if "logs/" in filename:
                filename = filename.replace('logs/', '')
            filename.strip()
            data = parts[2].strip()

            filenamedata = filename.split('_')
            lineout['pcap'] = filenamedata[1].replace('.pcap', '')
            lineout['nclients'] = filenamedata[2]
            lineout['nactiveclients'] = filenamedata[3]
            lineout['repeat'] = filenamedata[4]
            lineout['data'] = data.split(';')

            json.append(lineout)

            if lineout['pcap'] not in pcapsNames:
                pcapsNames.append(lineout['pcap'])
            if lineout['nclients'] not in nClientsVals:
                nClientsVals.append(lineout['nclients'])
            if lineout['nactiveclients'] not in nActiveClientsVals:
                nActiveClientsVals.append(lineout['nactiveclients'])

            #print lineout

if len(sys.argv) < 2:
    print "Argument 1 must be the input file"
    sys.exit(1)

a = str(sys.argv[1])
parseGreppedToObject(a)

for pcap in pcapsNames:
    for nactiveclient in nActiveClientsVals:

        mergedData = {}

        for line in json:
            if line['pcap'] == pcap and line['nactiveclients'] == nactiveclient:

                if not line['nclients'] in mergedData:
                    mergedData[line['nclients']] = []


                mergedData[line['nclients']].extend(filter(is_number, line['data']))

        od = collections.OrderedDict(sorted(mergedData.items()))

        for nclients, data in od.items():
            with open("individualpcaps_"+pcap+"_"+nactiveclient+"_"+nclients+".gnudata", "w") as file:
                for v in data:
                    file.write(v+",\n")