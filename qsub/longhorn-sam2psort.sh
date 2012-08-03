#!/bin/bash
#$ -V                   # Inherit the submission environment
#$ -cwd                 # Start job in submission directory
#$ -o $JOB_NAME.o$JOB_ID # Name of the output file (eg. myMPI.oJobID)
#$ -j y 
#$ -pe 1way 8 # Requests 16 tasks/node, 32 cores total
#$ -q long
#$ -l h_rt=24:00:00     # Run time (hh:mm:ss)
#$ -M $EMAIL
#$ -m be		# Email at Begin and End of job
#$ -P hpc
set -x                  # Echo commands, use "set echo" with csh

#$ -N psrt_rfx2M2
#SAM="SA11049_XENLA_C1_JA11192tgacca.paired.Chung201110_XENLA_cdna_final.bowtie.sam_hit"
#SAM="SA11049_XENLA_C2_JA11192gccaat.paired.Chung201110_XENLA_cdna_final.bowtie.sam_hit"
#SAM="SA11049_XENLA_M1_JA11192acagtg.paired.Chung201110_XENLA_cdna_final.bowtie.sam_hit"
SAM="SA11049_XENLA_M2_JA11192acagtg.paired.Chung201110_XENLA_cdna_final.bowtie.sam_hit"

OUT=$SAM"_psort"
awk -F"\t" '{print $1"\t"$2"\t"$3"\t"$4"\t"$6"\t"$13"\t"$14}' $SAM | sort -k 3 -k 1 -T $SCRATCH > $OUT
