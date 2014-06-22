#!/bin/bash
SAMTOOLS="$HOME/src.HTseq/samtools/samtools-0.1.16/samtools"
BCFTOOLS="$HOME/src.HTseq/samtools/samtools-0.1.16/bcftools/bcftools"
DB="$SCRATCH/BACSU_trp/genome/168/BACSU_168.genome.fa"

for BAM in $(ls *.sorted.bam)
do
  VCF=${BAM/.sorted.bam/}".raw.vcf"
  $SAMTOOLS mpileup -uf $DB $BAM | $BCFTOOLS view -vcg - > $VCF
done
