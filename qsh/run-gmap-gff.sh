#!/bin/bash

#SBATCH -o gm.o%j
#SBATCH -J "gm."
#$ -N gmap.

GMAP="$HOME/local/bin/gmap"
GMAPDB="$SCRATCH/xenopus.db/GMAPDB/"
NUM_THREADS=1

FA="Ueno201302_XENLA_stage.cdna_full.fa"
DB="XENLA_JGIv7b"

OUT=${FA/.fa/}"."$DB".gmap_gff"
time $GMAP -f gff3_gene -t $NUM_THREADS -D $GMAPDB -d $DB $FA > $OUT
