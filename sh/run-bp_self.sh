#!/bin/bash
#SBATCH -o bpS.o%j
#SBATCH -J "bpS.foo"

#$ -N bpS.foo

## Thread: lonestar=12, stampede=16
NUM_THREADS=12

BLASTP="$HOME/src/blast+/bin/blastp -evalue 1e-4 -num_threads $NUM_THREADS -seg yes "
MKDB="$HOME/src/blast+/bin/makeblastdb"

FA="XENLA_prot_v5_trio.fa"
DB=${FA/.fa/}

$MKDB -dbtype prot -in $FA -out $DB

OUT=$DB'.self.bp+_tbl'
time $BLASTP -db $DB -query $FA -out $OUT -outfmt "7 qseqid sseqid pident length mismatch gapopen qlen qstart qend slen sstart send evalue bitscore"
