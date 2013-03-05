#!/bin/bash
for TBL in $(ls *tbn+_tbl)
do
  OUT=${TBL/tbn+_tbl/best_q}
  echo $OUT
  ~/git/HTseq-toolbox/post/tbn-to-best_q.py $TBL > $OUT
done
