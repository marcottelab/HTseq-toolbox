#!/bin/bash
for FASTQ in $(ls *.called.fastq)
do
  echo $FASTQ
  ~/git/HTseq-toolbox/fastq/fastq2pos.py $FASTQ
done
