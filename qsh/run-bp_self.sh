#!/bin/bash
BLASTP="$HOME/src/blast+/bin/blastp -evalue 1e-4 -num_threads 1 "
BEST="$HOME/git/HTseq-toolbox/blast/tbl-to-best_bitscore.py"

FA="XENLA_prot_v5_trio.fa"

DB=${FA/.fa/}
OUT=${FA/.fa/}'.self.bp+_tbl'
echo $FA" --> $OUT"
time $BLASTP -db $DB -query $FA -out $OUT -outfmt "7 qseqid sseqid pident length mismatch gapopen qlen qstart qend slen sstart send evalue bitscore"
$BEST $OUT
