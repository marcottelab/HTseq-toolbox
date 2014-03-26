#!/usr/bin/python
import os
import sys

filename_list = sys.argv[1]

sample_list = []
gene_list = []
g2s = dict()

f_list = open(filename_list,'r')
for line in f_list:
    tokens = line.strip().split("\t")
    sample_name = tokens[0]
    filename = tokens[1]
    if( not os.access(filename,os.R_OK) ):
        sys.stderr.write('%s is not available. Skip.\n'%filename)
        continue

    sample_list.append(sample_name)
    sys.stderr.write('Read %s as Sample %s... '%(filename,sample_name))
    f = open(filename,'r')
    f.readline()
    for line in f:
        if( line.startswith('#') ):
            continue
        tokens = line.strip().split('\t')
        gene_id = tokens[0]
        gene_list.append(gene_id)
        if(not g2s.has_key(gene_id) ):
            g2s[gene_id] = dict()
        g2s[gene_id][sample_name] = float(tokens[1])
    sys.stderr.write('Done\n')

sample_list = sorted(sample_list)
gene_list = sorted(list(set(gene_list)))
print "ID\t%s"%('\t'.join(sample_list))
for tmp_g in gene_list:
    out_list = [tmp_g]
    for tmp_s in sample_list:
        if( g2s[tmp_g].has_key(tmp_s) ):
            out_list.append('%.3f'%g2s[tmp_g][tmp_s])
        else:
            out_list.append('0.000')
    print "\t".join(out_list)
