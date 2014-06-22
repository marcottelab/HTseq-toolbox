#!/bin/bash

#SBATCH -o bw2.o%j
#SBATCH -J "bw2.foo"

#$ -N bw2.foo

BOWTIE2="$HOME/src.HTseq/bowtie/2.0.6/bowtie2"
SAM2HIT="$HOME/git/HTseq-toolbox/sam/sam-to-sam_hit.py"
SAM2FREQ="$HOME/git/HTseq-toolbox/sam/sam_hit-to-t_freq.py"

## Thread: lonestar=12, stampede=16
NUM_THREADS=12

export BOWTIE2_INDEXES="$WORK/ens/bw2"
#export BOWTIE_2INDEXES="$WORK/ens/bw1/"
#DB="XENLA_2013may_longest_cdna_annot"
#DB="XENLA_JGIv7b"
DB="MOUSE_ens72_cdna_annot_longest"

#FQ="../fastq/OMRF20110730_XENLA_EGG1.paired.fastq"
for FQ in $(ls ../fastq/*.fastq)
do
  BASENAME=$(basename $FQ)
  BASENAME=${BASENAME/.fastq/}"."$DB".bw2_k10N0"
  SAM=$BASENAME".sam"
  $BOWTIE2 -q --end2end -k 10 -N 0 --threads $NUM_THREADS --reorder -x $DB -U $FQ -S $SAM
  $SAM2HIT $SAM
  $SAM2FREQ $SAM"_hit"
done
