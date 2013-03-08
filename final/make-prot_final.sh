#!/bin/bash
for FA in $(ls *.prot_NR.fa)
do
  PART=${FA/.fa/.self.bp+_tbl_part}
  echo "$FA, $PART"
  $HOME/git/HTseq-toolbox/final/make-prot_final.py $FA $PART
done
