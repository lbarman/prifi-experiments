#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Argument 1 must be the file extention to remove (if empty)"
	exit 1;
fi

arg=$1

for f in ./*$arg; do
	if [ ! -s "$f" ]; then
		echo "Removing $f"
		rm "$f"
	fi
done
