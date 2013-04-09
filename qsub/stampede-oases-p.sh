#!/bin/bash
#SBATCH -n 16
#SBATCH -p largemem
#SBATCH -t 24:00:00
#SBATCH --mail-user=$EMAIL
#SBATCH -o op.o%j
# #SBATCH --mail-type=ALL

#SBATCH -J "op.V.K23"

OASES="$HOME/src.HTseq/oases/current/oases-101"
VELVETH="$HOME/src.HTseq/velvet/current/velveth-101"
VELVETG="$HOME/src.HTseq/velvet/current/velvetg-101"

FQ="../fastq/my.fastq"

for K in 23 27 31
#for K in 21 25 29
do
DIRNAME=$(basename $FQ)

DIRNAME=${DIRNAME/.paired.fastq/}
DIRNAME=$DIRNAME".K"$K"p"
$VELVETH $DIRNAME $K -shortPaired -fastq $FQ
$VELVETG $DIRNAME -read_trkg yes -ins_length 200 
$OASES $DIRNAME
done 
