#!/bin/bash
#$ -V
#$ -cwd
#$ -j y
#$ -o $JOB_NAME.o$JOB_ID
#$ -pe 1way 8
#$ -q normal
#$ -l h_rt=04:00:00
#$ -M $EMAIL
#$ -m be
#$ -P hpc
set -x
#$ -N oTx_NR

NR_SEQ="/home/00992/linusben/git/HTseq-toolbox/oTx/make-NR_seq.py"
for FA in $(ls *combined_oTx.fa)
do
  OUT=${FA/.fa/.NR_fa}
  if [ ! -e $OUT ]; then
    $NR_SEQ $FA
  fi
done
