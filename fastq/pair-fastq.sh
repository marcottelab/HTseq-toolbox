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
#$ -N p.J2oo

PAIR="pair-fastq.py"
for R1 in $(ls *.raw.fastq.gz)
do
  R2=${R1/_R1/_R2}
  OUT=${R1/_R1.raw.fastq.gz/_paired.fastq}
  $PAIR $R1 $R2 $OUT
done
