#!/bin/bash
#$ -V                   # Inherit the submission environment
#$ -cwd                 # Start job in submission directory
#$ -j y                 # Combine stderr and stdout
#$ -o $JOB_NAME.o$JOB_ID
#$ -pe 1way 8           # Requests 16 tasks/node, 32 cores total
#$ -q largemem		# Queue name "normal"
#$ -l h_rt=08:00:00     # Run time (hh:mm:ss)
#$ -M taejoon.kwon@marcottelab.org
#$ -m be                # Email at Begin and End of job
#$ -P hpc

set -x                  # Echo commands, use "set echo" with csh
OASES="/home/00992/linusben/src.HTseq/oases/current/oases-101"
VELVETH="/home/00992/linusben/src.HTseq/velvet/current/velveth-101"
VELVETG="/home/00992/linusben/src.HTseq/velvet/current/velvetg-101"

#$ -N oms.cap1a.K35
FA_m="../mfasta/my.mult_fasta"

FA_s=${FA_m/mult_fasta/single_fasta}

#for K in 27 29 31
for K in 35
do
  DIRNAME=$(basename $FA_m)
  DIRNAME=${DIRNAME/.mult_fasta/}".K"$K"ms"
  $VELVETH $DIRNAME $K -short -fasta $FA_m -short -fasta $FA_s
  $VELVETG $DIRNAME -read_trkg yes
  $OASES $DIRNAME
done
