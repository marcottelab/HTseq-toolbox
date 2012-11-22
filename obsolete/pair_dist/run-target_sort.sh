#!/bin/bash
S2T="$HOME/git/HTseq-toolbox/sam/sam-to-target_sort.py"

for SAM in $(ls *.sam_hit)
do
  OUT=${SAM/.sam_hit/.target_sort}
  $S2T $SAM | sort > $OUT
done
