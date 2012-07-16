#!/bin/bash
#$ -V                   # Inherit the submission environment
#$ -cwd                 # Start job in submission directory
#$ -o $JOB_NAME.o$JOB_ID # Name of the output file (eg. myMPI.oJobID)
#$ -j y 
#$ -pe 1way 8		# Requests 16 tasks/node, 32 cores total
#$ -q long
#$ -l h_rt=24:00:00     # Run time (hh:mm:ss)
#$ -M $EMAIL
#$ -m be		# Email at Begin and End of job
#$ -P hpc
set -x                  # Echo commands, use "set echo" with csh

SAM2SLIM="/home/00992/linusben/git/HTseq-toolbox/sam/sam-to-sam_hit.py"
BOWTIE="/home/00992/linusben/src.HTseq/bowtie/bowtie-0.12.7/bowtie"
export BOWTIE_INDEXES="$SCRATCH/xenopus/pancreas/bowtie"
DB="Jarikji201201_XENLA_cdna_final"

#$ -N bw_GFPd8.3
#FQ="../fastq/Jarkji201201_GFPdex4_1_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_GFPdex4_2_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_GFPdex4_3_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_GFPdex8_1_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_GFPdex8_2_J.paired_norep.fastq"
FQ="../fastq/Jarkji201201_GFPdex8_3_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_Ngn3GR_1_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_Ngn3GR_2_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_Ngn3GR_3_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_Ngn3GRdex4_1_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_Ngn3GRdex4_2_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_Ngn3GRdex4_3_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_Ngn3GRdex8_1_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_Ngn3GRdex8_2_J.paired_norep.fastq"
#FQ="../fastq/Jarkji201201_Ngn3GRdex8_3_J.paired_norep.fastq"

BASENAME=$(basename $FQ)
BASENAME=${BASENAME/.fastq/}".$DB.bowtie"
SAM=$BASENAME".sam"
$BOWTIE -q -a -n 2 -p 8 --sam $DB $FQ $SAM
$SAM2SLIM $SAM
