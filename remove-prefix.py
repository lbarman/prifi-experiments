import sys
import re

def processFile(inFile, outFile):
    linesOut = []
    with open(inFile) as file:
        rawData = file.read()
        lines = rawData.split("\n")
        for line in lines:
            line2 = ""
            if re.search("1 : time_statistics.go:87 \\(log.\\(\\*TimeStatistics\\)\\.ReportWithInfo\\)(\\s+)\\- ", line) is not None:
                line2 = re.sub("1 : time_statistics.go:87 \\(log.\\(\\*TimeStatistics\\)\\.ReportWithInfo\\)(\\s+)\\- ", "", line)
            elif re.search("1 : bw_statistics.go:107 \\(log.\\(\\*BitrateStatistics\\)\\.ReportWithInfo\\)(\\s+)\\- ", line) is not None:
                line2 = re.sub("1 : bw_statistics.go:107 \\(log.\\(\\*BitrateStatistics\\)\\.ReportWithInfo\\)(\\s+)\\- ", "", line)
            elif "ReportWithInfo: 114) - " in line:
                line2 = line[line.find("ReportWithInfo: 114) - ")+"ReportWithInfo: 114) - ".__len__():]
            elif "ReportWithInfo: 114) - " in line:
                line2 = line[line.find("ReportWithInfo: 114) - ")+"ReportWithInfo: 114) - ".__len__():]
            elif "StopMeasureAndLogWithInfo:  68) - " in line:
                line2 = line[line.find("StopMeasureAndLogWithInfo:  68) - ")+"StopMeasureAndLogWithInfo:  68) - ".__len__():]
            elif "log.(*BitrateStatistics).ReportWithInfo: 107) - " in line:
                line2 = line[line.find("log.(*BitrateStatistics).ReportWithInfo: 107) - ")+"log.(*BitrateStatistics).ReportWithInfo: 107) - ".__len__():]
            elif "ReceivedPcap:  60) - " in line:
                line2 = line[line.find("ReceivedPcap:  60) - ")+"ReceivedPcap:  60) - ".__len__():]
            if line2 != "":
                linesOut.append(line2)
    with open(outFile, "w") as file:
        for line in linesOut:
            file.write(line+"\n")


if len(sys.argv) < 2:
    print "Argument 1 must be the input file"
    sys.exit(1)

if len(sys.argv) < 3:
    print "Argument 2 must be the output file"
    sys.exit(1)


a = str(sys.argv[1])
b = str(sys.argv[2])
processFile(a, b)