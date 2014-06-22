#!/bin/bash

#SBATCH -o bw1.o%j
#SBATCH -J "bw1.foo"

#$ -N bw1.foo

BOWTIE="$HOME/src.HTseq/bowtie/1.0.0/bowtie"
SAM2HIT="$HOME/git/HTseq-toolbox/sam/sam-to-sam_hit.py"
SAM2FREQ="$HOME/git/HTseq-toolbox/sam/sam_hit-to-t_freq.py"

## Thread: lonestar=12, stampede=16
NUM_THREADS=12

export BOWTIE_INDEXES="$WORK/xenopus.db/bw1/"
#export BOWTIE_INDEXES="$WORK/ens/bw1/"
#DB="XENLA_2013may_longest_cdna_annot"
#DB="XENLA_JGIv7b"
DB="MOUSE_ens72_cdna_annot_longest"

#FQ="../fastq/OMRF20110730_XENLA_EGG1.paired.fastq"
FQ="../fastq/OMRF20110730_XENLA_EGG2.paired.fastq"

SAM=$(basename $FQ)
SAM=${SAM/.called.fastq/_called}
SAM=${SAM/.paired.fastq/_paired}
SAM=$SAM"."$DB".bw1_m5v2.sam"

$BOWTIE -m 5 -v 2 -p $NUM_THREADS --sam -q $DB $FQ $SAM
$SAM2HIT $SAM
$SAM2FREQ $SAM"_hit"
