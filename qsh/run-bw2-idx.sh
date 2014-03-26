#!/bin/bash

#SBATCH -o bw2i.o%j
#SBATCH -J "bw2i.foo"

#$ -N bw2i.foo

BW2_BUILD="$HOME/src.HTseq/bowtie/2.0.6/bowtie2-build"
FA="XENLA_JGIv7b.fa"

$BW2_BUILD $FA ${FA/.fa/}
