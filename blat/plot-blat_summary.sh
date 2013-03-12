#!/bin/bash
for SUM in $(ls *summary)
do
  echo $SUM
  $HOME/git/HTseq-toolbox/blat/plot-blat_summary.py $SUM
done
