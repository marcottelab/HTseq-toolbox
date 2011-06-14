#!/bin/bash
for SAM in $(ls *sam_slim)
do
#SAM=$1
  TFREQ=${SAM%".sam_slim"}".target_freq"
  echo "$SAM --> $TFREQ"
  grep ^[^@] $SAM | gawk -F"\t" '{print $3}' | sort | uniq -c | sort -k 1 -n > $TFREQ
done
