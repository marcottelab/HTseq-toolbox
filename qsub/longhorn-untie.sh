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

#$ -N ut_sp1nB
#FQ="TeperekTkacz201206_XENLA_pr1nA.paired.fastq"
#FQ="TeperekTkacz201206_XENLA_pr1nB.paired.fastq"
#FQ="TeperekTkacz201206_XENLA_sp1nA.paired.fastq"
FQ="TeperekTkacz201206_XENLA_sp1nB.paired.fastq"

~/git/HTseq-toolbox/fastq/untie-paired_fastq.py $FQ
