#!/bin/bash
BEDTOOLS="$HOME/src.HTseq/bedtools/2.17.0/bin/bedtools"
BG2BIGWIG="$HOME/src.HTseq/ucsc/bedGraphToBigWig"

for BAM in $(ls *bam)
do
  echo $BAM
  BG=${BAM/.bam/}".bedgraph"
  BIGWIG=${BAM/.bam/}".bigWig"
  SEQLEN="/work/PSEAE_net/genome/PSEAE_PA14_genome.seqlen"

  $BEDTOOLS genomecov -ibam $BAM -bg > $BG
  $BG2BIGWIG $BG $SEQLEN -blockSize=10 $BIGWIG
done
