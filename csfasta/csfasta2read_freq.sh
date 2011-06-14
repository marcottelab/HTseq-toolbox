#!/bin/bash

CSFASTA=$1
OUT=${CSFASTA%".csfasta"}".read_freq"
echo "$CSFASTA --> $OUT"
grep -P "^[^>]" $CSFASTA | sort | uniq -c | sort -nr > $OUT
