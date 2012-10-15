#!/bin/bash
REF_Q_SUM="$HOME/git/HTseq-toolbox/oTx/ref_q_bp_tbl-to-bp_summary.py"
REF_T_SUM="$HOME/git/HTseq-toolbox/oTx/ref_t_bp_tbl-to-bp_summary.py"

for REF_Q in $(ls ?????_*bp+_tbl)
do
  echo "REF_Q: "$REF_Q
  $REF_Q_SUM $REF_Q
done

for REF_T in $(ls *pep_final.?????_*bp+_tbl)
do
  echo "REF_T: "$REF_T
  $REF_T_SUM $REF_T
done
