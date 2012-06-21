#!/bin/bash
#$ -V                   # Inherit the submission environment
#$ -cwd                 # Start job in submission directory
#$ -j y                 # Combine stderr and stdout
#$ -o $JOB_NAME.o$JOB_ID # Name of the output file (eg. myMPI.oJobID)
#$ -pe 1way 16
#$ -q normal
#$ -l h_rt=24:00:00     # Run time (hh:mm:ss)
#$ -M $EMAIL
#$ -m be                # Email at Begin and End of job
#$ -P hpc
set -x                  # Echo commands, use "set echo" with csh

#$ -N fq2rfq
for FASTQ in $(ls *.called.fastq)
do
  CWD=$(dirname $0)
  OUT=${FASTQ%fastq}"read_freq"
  echo "$FASTQ --> $OUT"
  $HOME/git/HTseq-toolbox/fastq/fastq-to-nseq.py $FASTQ | sort -T $SCRATCH | uniq -c | sort -n -T $SCRATCH > $OUT
done
