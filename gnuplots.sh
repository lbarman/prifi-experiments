#!/bin/sh
for f in *.gnuplot; do
    echo "Trying $f (could fail if data is not there)"
    gnuplot "$f"
done

exit 0