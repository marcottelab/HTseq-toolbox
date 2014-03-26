#!/bin/bash
FA=$1

for TFREQ in $(ls *t_freq)
do
  $HOME/git/HTseq-toolbox/rpkm/t_freq+fa-to-rpkm.py $TFREQ $FA
done
