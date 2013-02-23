#!/bin/bash
BEST="$HOME/git/HTseq-toolbox/blast/tbl-to-best_bitscore.py"
for TBL in $(ls *_tbl)
do
  OUT=$TBL"_best"
  if [ ! -e $OUT ]; then
    echo $TBL
    $BEST $TBL
  fi
done
