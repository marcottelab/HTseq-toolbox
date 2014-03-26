#!/bin/bash

#SBATCH -o bp6r.o%j
#SBATCH -J "bp6r.foo"

#$ -N bp6r.foo

## Thread: lonestar=12, stampede=16
NUM_THREADS=12

BLASTP="$HOME/src/blast+/bin/blastp -evalue 1e-4 -num_threads $NUM_THREADS -seg yes "

FA="Evans201309_XENEP_BrainF01_NoPart_oTx_prot6.DANRE_ens72_prot_annot_longest.bp+_tbl.remains"
DB_DIR="$WORK/ens/72"

DB_NAME=$(ls $FA | awk -F"." '{print $2}')
DB=$DB_DIR"/"$DB_NAME

OUT=$FA".bp+_tbl"
time $BLASTP -db $DB -query $FA -out $OUT -outfmt "7 qseqid sseqid pident length mismatch gapopen qlen qstart qend slen sstart send evalue bitscore"

Q_count=$(grep 'Query:' $TBL | wc -l)
echo "$Q_count - $TBL" >> tbl_query.txt
