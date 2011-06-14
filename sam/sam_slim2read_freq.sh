#!/bin/bash
for SAM in $(ls *sam_slim)
do
#SAM=$1
  READFREQ=${SAM%".sam_slim"}".read_freq"
  echo "$SAM --> $READFREQ"
  grep ^[^@] $SAM | gawk -F"\t" '{print $1}' | sort | uniq -c | sort -k 1 -n > $READFREQ
done
