#!/bin/bash
#$ -V
#$ -cwd
#$ -j y
#$ -o $JOB_NAME.o$JOB_ID
#$ -pe 1way 16
#$ -q normal
#$ -l h_rt=24:00:00
#$ -M taejoon.kwon@gmail.com
#$ -m be
#$ -P hpc
set -x
BLASTP='/share/home/00992/linusben/src/blast+/bin/blastp -evalue 1e-4 -num_threads 16 '

#$ -N bp+Jti.CHICK

#FA="Amin201106_XENLA_pep_final.fa"
#FA="Chung201110_XENLA_pep_final.fa"
#FA="Ismailoglu201203_XENLA_pep_final.fa"
#FA="Jarikji201201_XENLA_pep_final.fa"
#FA="Park201106_XENLA_pep_final.fa"
#FA="Quigley201112_XENLA_pep_final.fa"
#FA="TeperekTkacz201202_XENLA_pep_final.fa"
#FA="TXGP201107_XENLA_pep_final.fa"
#FA="Veenstra201204_XENLA_pep_final.fa"
#FA="Taira201203_XENLA_stage_pep_final.fa"
FA="Taira201203_XENLA_tissue_pep_final.fa"

DBNAME="CHICK_ens66_pep_longest"
#DBNAME="DANRE_ens66_pep_longest"
#DBNAME="HUMAN_ens66_pep_longest"
#DBNAME="MOUSE_ens66_pep_longest"
#DBNAME="XENTR_ens66_pep_longest"
#DBNAME="XENLA_prot_v4"

DB="../../ens/66/"$DBNAME
OUT=${FA/.fa/}.$DBNAME".bp+_tbl"

$BLASTP -db $DB -query $FA -out $OUT -outfmt "7 qseqid sseqid pident length mismatch gapopen qlen qstart qend slen sstart send evalue bitscore"

