#!/bin/bash
#$ -V                   # Inherit the submission environment
#$ -cwd                 # Start job in submission directory
#$ -o $JOB_NAME.o$JOB_ID # Name of the output file (eg. myMPI.oJobID)
#$ -j y 
#$ -pe 1way 16 # Requests 16 tasks/node, 32 cores total
#$ -q normal
#$ -l h_rt=24:00:00     # Run time (hh:mm:ss)
#$ -M $EMAIL
#$ -m be		# Email at Begin and End of job
#$ -P hpc
set -x                  # Echo commands, use "set echo" with csh

#$ -N pdst_st15
#PSORT="Taira201203_XENLA_st01_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort"
#PSORT="Taira201203_XENLA_st08_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort"
#PSORT="Taira201203_XENLA_st09_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort"
#Taira201203_XENLA_st10_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort
#PSORT="Taira201203_XENLA_st12_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort"
PSORT="Taira201203_XENLA_st15_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort"
#Taira201203_XENLA_st20_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort
#Taira201203_XENLA_st25_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort
#Taira201203_XENLA_st30_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort
#Taira201203_XENLA_st35_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort
#Taira201203_XENLA_st40_paired.Taira201203_XENLA_stage_cdna_final.bowtie.sam_hit_psort

module load python
$HOME/git/HTseq-toolbox/sam/sam_psort-to-sam_pdist.py $PSORT
