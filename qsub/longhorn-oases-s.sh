#!/bin/bash
#$ -V                   # Inherit the submission environment
#$ -cwd                 # Start job in submission directory
#$ -j y                 # Combine stderr and stdout
#$ -o $JOB_NAME.o$JOB_ID
#$ -pe 1way 8           # Requests 16 tasks/node, 32 cores total
#$ -q largemem		# Queue name "normal"
#$ -l h_rt=08:00:00     # Run time (hh:mm:ss)
#$ -M $EMAIL
#$ -m be                # Email at Begin and End of job
#$ -P hpc

set -x                  # Echo commands, use "set echo" with csh
OASES="/home/00992/linusben/src.HTseq/oases/current/oases-101"
VELVETH="/home/00992/linusben/src.HTseq/velvet/current/velveth-101"
VELVETG="/home/00992/linusben/src.HTseq/velvet/current/velvetg-101"

#$ -N oms.capACA.K41
FQ="../fastq/my.fastq"

for K in 41
#for K in 27 29 31
#for K in 21 23 25
do
  DIRNAME=$(basename $FQ)
  DIRNAME=${DIRNAME/.called.fastq/}".K"$K"s"
  $VELVETH $DIRNAME $K -short -fastq $FQ
  $VELVETG $DIRNAME -read_trkg yes
  $OASES $DIRNAME
done
