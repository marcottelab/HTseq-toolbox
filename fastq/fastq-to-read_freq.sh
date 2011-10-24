#!/bin/bash
for FASTQ in $(ls *.fastq)
do
  CWD=$(dirname $0)
  OUT=${FASTQ%fastq}"read_freq"
  echo "$FASTQ --> $OUT"
  $CWD/fastq-to-nseq.py $FASTQ | sort | uniq -c | sort -n > $OUT
done
