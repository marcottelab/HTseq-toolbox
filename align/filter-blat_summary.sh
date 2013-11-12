#!/bin/bash
for SUM in $(ls *summary)
do
  echo $SUM
  $HOME/git/HTseq-toolbox/blat/filter-blat_summary.py $SUM
done
