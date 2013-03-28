#!/bin/bash
for FASTQ in $(ls *raw.fastq*)
do
  echo $FASTQ
  ~/git/HTseq-toolbox/fastq/filter-nocall.py $FASTQ
done
