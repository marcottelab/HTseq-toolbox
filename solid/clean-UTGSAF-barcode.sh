#!/bin/bash
for CSFASTA in $(ls *csfasta*)
do
  echo $CSFASTA
  /home/taejoon/git/HTseq-toolbox/UTGSAF/clean-barcode.py $CSFASTA
done
