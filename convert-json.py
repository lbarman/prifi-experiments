import sys
import re
import json

regex1str = "\[([\d]+)\] ([\d\.]+) round\/sec, ([\d\.]+) kB\/s up, ([\d\.]+) kB\/s down, ([\d\.]+) kB\/s down\(udp\), ([\d\.]+) kB\/s down\(re-udp\)"
regex1 = re.compile(regex1str)
regex2str = "\[([-\d]+)\] ([-\d\.]+) ms \+- ([-\d\.]+) \(over ([-\d\.]+), happened ([-\d\.]+)\)\. Info: ([\w\-_]+)"
regex2 = re.compile(regex2str)
regex3str = "\[StopMeasureAndLog\] measured time for ([\w\-_]+) : ([\d\.]+) ns, info: ([\w\-_]+)"
regex3 = re.compile(regex3str)
regex4str = "Received pcap ([\d\.]+) ([\d\.]+) ([\d\.]+)"
regex4 = re.compile(regex4str)

def processFile(inFile, outFile):
    data = []
    with open(inFile) as file:
        rawData = file.read()
        lines = rawData.split("\n")

        #find the last report, i.e. the steady state
        maxReportId = -1
        for line in lines:
            reportIdMatches = re.findall("\[([\d]+)\]", line)
            if len(reportIdMatches) == 0:
                continue
            reportId = reportIdMatches[0]
            if int(reportId) > maxReportId:
                maxReportId = int(reportId)

        #print "Max report id is "+str(maxReportId)

        # filter by latest report (most stable)
        interestingData = []
        for line in lines:
            if "[0]" not in line and "[1]" not in line:
                interestingData.append(line)

        # parse the data
        for line in interestingData:
            parsed = regex1.findall(line)
            if len(parsed) > 0:
                parsed = parsed[0]
                throughputData = {}
                throughputData["reportId"] = parsed[0]
                throughputData["round_s"] = parsed[1]
                throughputData["tp_up"] = parsed[2]
                throughputData["tp_down"] = parsed[3]
                throughputData["tp_udp_down"] = parsed[4]
                throughputData["tp_udp_re_down"] = parsed[5]
                data.append(throughputData)
            parsed = regex2.findall(line)
            if len(parsed) > 0:
                parsed = parsed[0]
                durationData = {}
                durationData["reportId"] = parsed[0]
                durationData["duration_mean"] = parsed[1]
                durationData["duration_conf"] = parsed[2]
                durationData["nsamples"] = parsed[3]
                durationData["popsize"] = parsed[4]
                durationData["text"] = parsed[5]
                data.append(durationData)
            parsed = regex3.findall(line)
            if len(parsed) > 0:
                parsed = parsed[0]
                timingData = {}
                timingData["measure_name"] = parsed[0]
                timingData["duration_ns"] = parsed[1]
                timingData["info"] = parsed[2]
                data.append(timingData)
            parsed = regex4.findall(line)
            if len(parsed) > 0:
                parsed = parsed[0]
                timingData = {}
                timingData["pcap_id"] = parsed[0]
                timingData["pcap_time_diff"] = parsed[1]
                timingData["pcap_size"] = parsed[2]
                data.append(timingData)

    with open(outFile, "w") as file:
        file.write("[")
        for line in data:
            file.write(json.dumps(line, sort_keys=False)+",\n")
        file.write("]")


if len(sys.argv) < 2:
    print "Argument 1 must be the input file"
    sys.exit(1)

if len(sys.argv) < 3:
    print "Argument 2 must be the output file"
    sys.exit(1)


a = str(sys.argv[1])
b = str(sys.argv[2])
processFile(a, b)