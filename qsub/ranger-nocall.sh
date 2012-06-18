#!/bin/bash
#$ -V
#$ -cwd
#$ -j y
#$ -o $JOB_NAME.o$JOB_ID
#$ -pe 1way 16
#$ -q normal
#$ -l h_rt=24:00:00
#$ -M taejoon.kwon@gmail.com
#$ -m be
#$ -P hpc
set -x
NC="/share/home/00992/linusben/git/HTseq-toolbox/fastq/filter-nocall.py"

#$ -N nocall_WT2n2

for FQ in $(ls Sample*fastq)
do
  $NC $FQ
done
