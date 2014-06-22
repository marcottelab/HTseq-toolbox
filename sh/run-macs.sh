#!/bin/bash

## For SLURM - stampede, maverick
#SBATCH -o mcs.o%j
#SBATCH -J "mcs.foo"

## For SGE - lonestar
#$ -N mcs.foo

if command -v module 2>/dev/null; then
  module load python
fi

MACS="$HOME/local/bin/macs14"
SAMTOOLS="$HOME/src.HTseq/samtools/0.1.16/samtools"

export PYTHONPATH=$PYTHONPATH:$HOME/local/lib/python2.7/site-packages/

CTRL_SAM="Control sam file"
TARGET_SAM="Target sam file"
NAME="output_name"

CTRL_BAM=${CTRL_SAM/.sam_hit/}".bam"
CTRL_BAM=${CTRL_BAM/.sam/".bam"
TARGET_BAM=${TARGET_SAM/.sam_hit/}".bam"
TARGET_BAM=${TARGET_BAM/.sam/}".bam"

$SAMTOOLS view -Sb -o $CTRL_BAM $CTRL_SAM
$SAMTOOLS view -Sb -o $TARGET_BAM $TARGET_SAM

$MACS -t $TARGET_BAM -c $CTRL_BAM -f BAM -g hs -n $NAME -w 
