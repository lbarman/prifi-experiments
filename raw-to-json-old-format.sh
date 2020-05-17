#!/bin/bash

cd logs;

for f in experiment_*.txt; do
    echo "Processing $f"
    cat "$f" | grep "ReportWithInfo\|StopMeasureAndLogWithInfo\|ReceivedPcap" > "$f".parsed1
    if [ -f "$f".parsed1 ]; then
        python2 ../../remove-prefix-old-format.py "$f".parsed1 "$f".parsed2
    fi
    if [ -f "$f".parsed2 ]; then
        python2 ../../convert-json.py "$f".parsed2 "$f".json
    fi
done

rm *.parsed1
rm *.parsed2

for f in *.txt.json; do 
    mv -- "$f" "${f%.txt.json}.json"
done
