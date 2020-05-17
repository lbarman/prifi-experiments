#!/bin/bash

for f in *.eps; do
	epstopdf "$f"
done

exit 0