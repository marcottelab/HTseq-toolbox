#!/bin/bash
for FASTQ in $(ls *fastq)
do
  echo $FASTQ
  ~/git/HTseq-toolbox/fastq/filter-nocall.py $FASTQ
done

for FASTQz in $(ls *fastq.gz)
do
  echo $FASTQz
  ~/git/HTseq-toolbox/fastq/filter-nocall.py $FASTQz
done
