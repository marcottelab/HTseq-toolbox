#!/bin/bash
#$ -V                   # Inherit the submission environment
#$ -cwd                 # Start job in submission directory
#$ -o $JOB_NAME.o$JOB_ID # Name of the output file (eg. myMPI.oJobID)
#$ -j y 
#$ -pe 1way 8
#$ -q largemem
#$ -l h_rt=08:00:00     # Run time (hh:mm:ss)
#$ -M $EMAIL
#$ -m be		# Email at Begin and End of job
#$ -P hpc
set -x                  # Echo commands, use "set echo" with csh

#$ -N pdst_M2
#PSORT="SA11049_XENLA_C1_JA11192tgacca.paired.Chung201110_XENLA_cdna_final.bowtie.sam_hit_psort"
#PSORT="SA11049_XENLA_C2_JA11192gccaat.paired.Chung201110_XENLA_cdna_final.bowtie.sam_hit_psort"
#PSORT="SA11049_XENLA_M1_JA11192acagtg.paired.Chung201110_XENLA_cdna_final.bowtie.sam_hit_psort"
PSORT="SA11049_XENLA_M2_JA11192acagtg.paired.Chung201110_XENLA_cdna_final.bowtie.sam_hit_psort"

$HOME/git/HTseq-toolbox/sam/sam_psort-to-sam_pdist.py $PSORT
