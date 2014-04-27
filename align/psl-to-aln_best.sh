#!/bin/bash
for PSL in $(ls *_psl*)
do
  echo $PSL
  $HOME/git/HTseq-toolbox/align/psl-to-aln_best.py $PSL
done
