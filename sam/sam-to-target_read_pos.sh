#!/bin/bash
for SAM in $(ls *.sam*)
do
  OUT=${SAM/.sam*/}".target_read_pos"
  if [ -e $OUT ]; then
    echo "Skip $OUT"
  else
    echo "$SAM --> $OUT"
    awk '{print $3" _::_ "$1"\t"$4"\t"$2}' $SAM | sort > $OUT
  fi
done
