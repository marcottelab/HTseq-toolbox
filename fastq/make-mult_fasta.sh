#!/bin/bash
for RF in $(ls *read_freq)
do
  CWD=$(dirname $0)
  echo $RF
  $CWD/make-mult_fasta.py $RF
done
