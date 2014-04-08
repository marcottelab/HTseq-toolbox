#!/bin/bash

#SBATCH -o gm.o%j
#SBATCH -J "gm."
#$ -N gmap.

GMAP="$HOME/local/bin/gmap"
GMAP_BUILD="$HOME/local/bin/gmap_build"

FA="Ueno201302_XENLA_stage.cdna_full.fa"
NUM_THREADS=1

GMAPDB="."
DB=$FA
DBNAME=${FA/.fa/}

$HOME/local/bin/gmap_build 
$GMAP_BUILD -d $DBNAME $DB -D $GMAPDB

OUT=$DBNAME".self.gmap_psl"
time $GMAP -f psl -t $NUM_THREADS -D $GMAPDB -d $DB $FA > $OUT
