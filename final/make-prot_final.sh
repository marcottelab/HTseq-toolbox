#!/bin/bash
for FA in $(ls *.prot_NR.fa)
do
  PART=${FA/.fa/.self.bp+_tbl_part}
  echo "$FA, $PART"
  ./make-prot_final.py $FA $PART
done
