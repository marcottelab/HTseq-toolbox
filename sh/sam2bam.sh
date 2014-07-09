#!/bin/bash
SAMTOOLS="$HOME/src.HTseq/samtools/0.1.16/samtools"

for SAM in $(ls *sam_hit)
do
  echo $SAM
  BAM=${SAM/.sam_hit/}".bam"
  SORTED=${SAM/.sam_hit/}".sorted"
  INDEX=${SAM/.sam_hit/}".sorted.bai"
  $SAMTOOLS view -bS -o $BAM $SAM
  $SAMTOOLS sort $BAM $SORTED
  $SAMTOOLS index $SORTED".bam" $INDEX
done
