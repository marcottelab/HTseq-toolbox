#!/bin/bash
#$ -V
#$ -cwd
#$ -j y
#$ -o $JOB_NAME.o$JOB_ID
#$ -pe 1way 8
#$ -q long
#$ -l h_rt=24:00:00
#$ -M $EMAIL
#$ -m be
#$ -P hpc

set -x
EX="/home/00992/linusben/src/exonerate/exonerate-2.2.0-x86_64/bin/exonerate"

#$ -N ex.tissue.e
#FA="Taira201203_XENLA_tissue_cdna_final.part.aa"
#FA="Taira201203_XENLA_tissue_cdna_final.part.ab"
#FA="Taira201203_XENLA_tissue_cdna_final.part.ac"
#FA="Taira201203_XENLA_tissue_cdna_final.part.ad"
FA="Taira201203_XENLA_tissue_cdna_final.part.ae"

DB="/home/00992/linusben/scratch/xenopus.db/JGI/XENLA_JGIv5.2011oct.fa"
OUT=$FA".XENLA_JGIv5.exonerate_pct80"

$EX -m est2genome --percent 80 -Q dna -T dna --showvulgar no --showcigar no --showalignment no --ryo "%qi %ti %tS %qal %qab %qae %tal %tab %tae %et %ei %ps %pi %s %C\n " $FA $DB > $OUT

