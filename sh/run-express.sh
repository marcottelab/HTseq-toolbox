#!/bin/bash
EXPRESS="$HOME/src.HTseq/express/1.5.1/express"
#FA="$HOME/scratch/xenopus.db/XENLA_JGIv16_primTrs.fa"

#FA="/work/00992/linusben/ens/bw1/CHICK_ens72_cdna_annot_longest.fa"
#FA="/work/00992/linusben/ens/bw1/DANRE_ens72_cdna_annot_longest.fa"
#FA="/work/00992/linusben/ens/bw1/HUMAN_ens72_cdna_annot_longest.fa"
#FA="/work/00992/linusben/ens/bw1/MOUSE_ens72_cdna_annot_longest.fa"
FA="/work/00992/linusben/ens/bw1/XENTR_ens72_cdna_annot_longest.fa"

for BAM in $(ls *.sorted.bam)
do
  XPRS=${BAM/.bam/}".xprs"
  $EXPRESS --f-stranded $FA $BAM
  mv results.xprs $XPRS
done
