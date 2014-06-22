#!/bin/bash
#SBATCH -o pbS.o%j
#SBATCH -J "pbS.foo"

#$ -N pbS.foo

BLAT="$HOME/src/blat/blat"

FA="XENLA_prot_v5.fa"
DB=$FA
PSL=${FA/.fa/}".self.pblat_psl"

$BLAT -prot $DB $FA $PSL
