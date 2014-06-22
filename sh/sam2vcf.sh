#!/bin/bash
SAMTOOLS="$HOME/src.HTseq/samtools/samtools-0.1.16/samtools"
BCFTOOLS="$HOME/src.HTseq/samtools/samtools-0.1.16/bcftools/bcftools"
DB="$SCRATCH/BACSU_trp/genome/168/BACSU_168.genome.fa"

for SAM in $(ls *.sam_hit)
do
  BAM=${SAM/.sam_hit/}".bam"
  SORTED_BAM=${SAM/.sam_hit/}".sorted"
  VCF=${SAM/.sam_hit/}".raw.vcf"
  $SAMTOOLS view -bS $SAM > $BAM
  $SAMTOOLS sort $BAM $SORTED_BAM
  SORTED_BAM=$SORTED_BAM".bam"
  $SAMTOOLS mpileup -uf $DB $SORTED_BAM | $BCFTOOLS view -vcg - > $VCF
done
