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
#$ -N uc.Tst10

USEARCH="/home/00992/linusben/src/usearch/current"

#FA_L="Taira201203_XENLA_egg.combined_oTx.NR_lt1k_fa"
#FA_L="Taira201203_XENLA_st08.combined_oTx.NR_lt1k_fa"
#FA_L="Taira201203_XENLA_st09.combined_oTx.NR_lt1k_fa"
FA_L="Taira201203_XENLA_st10.combined_oTx.NR_lt1k_fa"
#FA_L="Taira201203_XENLA_st12.combined_oTx.NR_lt1k_fa"
#FA_L="Taira201203_XENLA_st15.combined_oTx.NR_lt1k_fa"
#FA_L="Taira201203_XENLA_st20.combined_oTx.NR_lt1k_fa"
#FA_L="Taira201203_XENLA_st25.combined_oTx.NR_lt1k_fa"
#FA_L="Taira201203_XENLA_st30.combined_oTx.NR_lt1k_fa"
#FA_L="Taira201203_XENLA_st35.combined_oTx.NR_lt1k_fa"
#FA_L="Taira201203_XENLA_st40.combined_oTx.NR_lt1k_fa"

BASENAME=$(basename $FA_L)
BASENAME=${BASENAME/.combined_oTx.NR_lt1k_fa/}

NR_FA=$BASENAME".ucNR_lt1k.fa"
UC=$BASENAME".ucNR_lt1k_uc099"

time $USEARCH -cluster_smallmem $FA_L -id 0.99 -centroids $NR_FA -uc $UC
