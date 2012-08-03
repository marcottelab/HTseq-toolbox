#!/bin/bash
#$ -V
#$ -cwd
#$ -j y
#$ -o $JOB_NAME.o$JOB_ID
#$ -pe 1way 8
#$ -q long
#$ -l h_rt=24:00:00
#$ -M $EMAIL
#$ -m be
#$ -P hpc
set -x
TIE="/home/00992/linusben/git/HTseq-toolbox/fastq/tie-flash_fastq.py"

#$ -N tie_egg
for FQ in $(ls *notCombined_1.fastq)
do
  NAME=${FQ/.notCombined_1.fastq/}
  $TIE $NAME
done
