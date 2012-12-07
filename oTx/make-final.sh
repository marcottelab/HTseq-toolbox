#!/bin/bash
for PFA in $(ls *prot_NR.fa)
do
  echo $PFA
  ~/git/HTseq-toolbox/oTx/make-final.py $PFA
done
