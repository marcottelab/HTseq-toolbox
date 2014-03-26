#!/usr/bin/python
import os
import sys
import math

filename_edgeR_et = sys.argv[1]

pval_cutoff = 0.05
fold_cutoff = 2

log2FC_cutoff = math.log(fold_cutoff)/math.log(2)

f_edgeR_et = open(filename_edgeR_et,'r')
f_edgeR_et.readline()
for line in f_edgeR_et:
    tokens = line.strip().replace('"','').split("\t")
    tmp_id = tokens[0]
    
    tmp_log2FC = float(tokens[1])
    tmp_pval = float(tokens[4])

    if( tmp_pval < pval_cutoff and abs(tmp_log2FC) > log2FC_cutoff ):
        print "%s\t%.2f\t%.4f"%(tmp_id,tmp_log2FC,tmp_pval)
f_edgeR_et.close()
