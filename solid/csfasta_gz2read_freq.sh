#!/bin/bash

CSFASTA_GZ=$1
OUT=${CSFASTA_GZ%".csfasta.gz"}".read_freq"
echo "$CSFASTA_GZ --> $OUT"
zgrep -P "^[^>]" $CSFASTA_GZ | sort | uniq -c | sort -nr > $OUT
