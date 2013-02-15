#!/bin/bash
for FA in $(ls *.combined_oTx.NR_fa)
do
  PART=${FA/.NR_fa/_NR.self.mb+_tbl_part}
  $HOME/git/HTseq-toolbox/blast/make-NoPart_oTx.py $FA $PART
done
