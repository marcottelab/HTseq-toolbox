#!/bin/bash
for SAM in $(ls *sam_slim)
do
#SAM=$1
  BAM=${SAM%".sam_slim"}".bam"
  BAM_SORTED=${SAM%".sam_slim"}".sorted"
  echo "$SAM --> $BAM"
  samtools view -b -S $SAM > $BAM
  samtools sort $BAM $BAM_SORTED
  samtools index $BAM_SORTED".bam"
done
