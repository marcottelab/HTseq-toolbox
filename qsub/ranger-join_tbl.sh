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
TBL2FQ="$HOME/git/HTseq-toolbox/fastq/fastq_tbl_join-to-fastq.py"

#$ -N paired
for TBL_R1 in $(ls *_R1.called.fastq_tbl)
do
  TBL_R2=${TBL_R1/_R1.called.fastq_tbl/_R2.called.fastq_tbl}
  TBL_J=${TBL_R1/_R1.called.fastq_tbl/_J.fastq_tbl}
  FQ=${TBL_R1/_R1.called.fastq_tbl/.paired.fastq}
  join $TBL_R1 $TBL_R2 > $TBL_J
  $TBL2FQ $TBL_J > $FQ
done
