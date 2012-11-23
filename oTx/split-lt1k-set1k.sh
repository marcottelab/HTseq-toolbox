#!/bin/bash
for NR_FA in $(ls *NR_fa)
do
  echo $NR_FA
  $HOME/git/HTseq-toolbox/oTx/split-lt1k-set1k.py $NR_FA
done
