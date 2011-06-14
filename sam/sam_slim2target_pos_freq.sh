#!/bin/bash
for SAM in $(ls *sam_slim)
do
#SAM=$1
  TFREQ=${SAM%".sam_slim"}".target_pos_freq"
  echo "$SAM --> $TFREQ"
  grep ^[^@] $SAM | gawk -F"\t" '{print $3"\t"$4"\t"$2}' | sort | uniq -c | sort -k 1 -n > $TFREQ
done
