#!/bin/bash
for PROT_F in $(ls *.prot_final.fa)
do
  CDNA_NR=${PROT_F/.prot_final.fa/.cdna_NR.fa}
  echo $PROT_F
  $HOME/git/HTseq-toolbox/final/make-cdna_final.py $PROT_F $CDNA_NR
done
