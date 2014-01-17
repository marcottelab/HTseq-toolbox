#!/bin/bash
for TOP2 in $(ls *top2 )
do
  echo $TOP2
  $HOME/git/HTseq-toolbox/align/plot-top2.py $TOP2
done
