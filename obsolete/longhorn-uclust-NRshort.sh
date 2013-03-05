#!/bin/bash
#$ -V
#$ -cwd
#$ -j y
#$ -o $JOB_NAME.o$JOB_ID
#$ -pe 1way 8
#$ -q largemem
#$ -l h_rt=08:00:00
#$ -M $EMAIL
#$ -m be
#$ -P hpc
set -x
#$ -N ucS.Tegg

USEARCH="/home/00992/linusben/src/usearch/current"

FA_S="Taira201203_XENLA_egg.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st08.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st09.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st10.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st12.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st15.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st20.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st25.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st30.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st35.combined_oTx.NR_set1k_fa"
#FA_S="Taira201203_XENLA_st40.combined_oTx.NR_set1k_fa"

BASENAME=$(basename $FA_S)
BASENAME=${BASENAME/.combined_oTx.NR_set1k_fa/}

NR_FA=$BASENAME".ucNR_set1k.fa"
UC=$BASENAME".ucNR_set1k_uc099"

time $USEARCH -cluster_smallmem $FA_S -id 0.99 -centroids $NR_FA -uc $UC
