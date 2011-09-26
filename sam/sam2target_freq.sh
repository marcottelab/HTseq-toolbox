#!/bin/bash
for SAM in $(ls *.sam)
do
  TARGET_FREQ=${SAM%.sam}".target_freq"
  echo "$SAM --> $TARGET_FREQ"
  gawk -F"\t" '{print $3"\t"$4"\t"$2"\t"$6}' $SAM | sort | uniq -c | sort -k 2,2 -k 3,3n > $TARGET_FREQ
done
