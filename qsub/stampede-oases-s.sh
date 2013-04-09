#!/bin/bash
#SBATCH -n 16
#SBATCH -p largemem
#SBATCH -t 24:00:00
#SBATCH --mail-user=$EMAIL
#SBATCH -o sbatch.o%j
# #SBATCH --mail-type=ALL

#SBATCH -J "os.cap1C.K543"

OASES="$HOME/src.HTseq/oases/current/oases-101"
VELVETH="$HOME/src.HTseq/velvet/current/velveth-101"
VELVETG="$HOME/src.HTseq/velvet/current/velvetg-101"

FQ="../fastq/my.fastq"

for K in 55 45 35
do
DIRNAME=$(basename $FQ)
DIRNAME=${DIRNAME/.called.fastq/}
DIRNAME=$DIRNAME".K"$K"s"
$VELVETH $DIRNAME $K -short -fastq $FQ 
$VELVETG $DIRNAME -read_trkg yes
$OASES $DIRNAME
done 
