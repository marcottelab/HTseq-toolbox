#!/bin/bash

#SBATCH -o bp6.o%j
#SBATCH -J "bpGG.foo"

#$ -N bpGG.foo

## Thread: lonestar=12, stampede=16
NUM_THREADS=12

BLASTP="$HOME/src/blast+/bin/blastp -evalue 1e-4 -num_threads $NUM_THREADS -seg yes "

FA="Evans201309_XENEP_LiverF01_NoPart_oTx_prot6.fa"

#DB="$WORK/ens/72/CHICK_ens72_prot_annot_longest.pin"
#DB="$WORK/ens/72/DANRE_ens72_prot_annot_longest.pin"
#DB="$WORK/ens/72/HUMAN_ens72_prot_annot_longest.pin"
#DB="$WORK/ens/72/MOUSE_ens72_prot_annot_longest.pin"
DB="$WORK/ens/72/XENTR_ens72_prot_annot_longest.pin"

DB=${DB/.pin/}
DBNAME=$(basename $DB)
TBL=${FA/.fa/}"."$DBNAME".bp+_tbl"
time $BLASTP -db $DB -query $FA -out $TBL -outfmt "7 qseqid sseqid pident length mismatch gapopen qlen qstart qend slen sstart send evalue bitscore"

Q_count=$(grep 'Query:' $TBL | wc -l)
echo "$Q_count - $TBL" >> tbl_query.txt
