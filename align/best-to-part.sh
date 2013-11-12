#!/bin/bash
for BEST in $(ls *best)
do
  echo $BEST
  ~/git/HTseq-toolbox/blast/best-to-part.py $BEST
done
