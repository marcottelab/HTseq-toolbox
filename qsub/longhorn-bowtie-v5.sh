#!/bin/bash
#$ -V                   # Inherit the submission environment
#$ -cwd                 # Start job in submission directory
#$ -o $JOB_NAME.o$JOB_ID # Name of the output file (eg. myMPI.oJobID)
#$ -j y 
#$ -pe 2way 16		# Requests 16 tasks/node, 32 cores total
#$ -q long
#$ -l h_rt=24:00:00     # Run time (hh:mm:ss)
#$ -M $EMAIL
#$ -m be		# Email at Begin and End of job
#$ -P hpc
set -x                  # Echo commands, use "set echo" with csh

SAM2SLIM="/home/00992/linusben/git/HTseq-toolbox/sam/sam-to-sam_hit.py"
BOWTIE="/home/00992/linusben/src.HTseq/bowtie/bowtie-0.12.7/bowtie"
export BOWTIE_INDEXES="$SCRATCH/xenopus.db/bowtie"
DB="Marcotte201204_DENTI_cdna_final"

#$ -N bw_body
FQ="../fastq/Marcotte201204_DENTI_TadpoleBody.paired.fastq"
#FQ="../fastq/Marcotte201204_DENTI_TadpoleHead.paired.fastq"

BASENAME=$(basename $FQ)
BASENAME=${BASENAME/.fastq/}".$DB.bowtie"
SAM=$BASENAME".sam"
$BOWTIE -q -a -v 5 -p 8 --sam $DB $FQ $SAM
$SAM2SLIM $SAM
rm $SAM
rm $SAM"_nohit"
/home/00992/linusben/git/HTseq-toolbox/sam/sam_hit-to-t_freq.py $SAM"_hit"
