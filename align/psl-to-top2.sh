#!/bin/bash
for PSL in $(ls *psl)
do
  echo $PSL
  $HOME/git/HTseq-toolbox/align/psl-to-top2.py $PSL
done
