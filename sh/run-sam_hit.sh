#!/bin/bash
SAM2HIT="$HOME/git/HTseq-toolbox/sam/sam-to-sam_hit.py"

for SAM in $(ls *sam.gz)
do
  echo $SAM
  $SAM2HIT $SAM
done
