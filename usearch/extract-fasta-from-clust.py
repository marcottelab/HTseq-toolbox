#!/usr/bin/python
import os
import sys
import gzip

filename_uc = sys.argv[1]
filename_fa = sys.argv[2]

clusters = dict()
clusters_stat = dict()

f_uc = open(filename_uc,'r')
if( filename_uc.endswith('.gz') ):
    f_uc = gzip.open(filename_uc,'rb')

for line in f_uc:
    if( line.startswith('S') ):
        tokens = line.strip().split("\t")
        clusters[ tokens[8] ] = []

    if( line.startswith('H') ):
        tokens = line.strip().split("\t")
        if( not clusters.has_key( tokens[9] ) ):
            clusters[ tokens[9] ] = []
        clusters[ tokens[9] ].append( tokens[8] )
    
    if( line.startswith('C') or line.startswith('D') ):
        tokens = line.strip().split("\t")
        pct_id = 100.0
        if( tokens[3] != '*' ):
            pct_id = float(tokens[3])
        clusters_stat[ tokens[8] ] = {'size':int(tokens[2]), 'pct_id':pct_id}
f_uc.close()

def read_fasta(filename):
    seq_list = dict()
    h = ''
    f = open(filename,'r')
    for line in f:
        if( line.startswith('>') ):
            h = line.strip().lstrip('>')
            seq_list[h] = []
        else:
            seq_list[h].append( line.strip() )
    f.close()

    return seq_list

#TXGP_EGG1_k41.transcripts.sorted_fasta
#TXGP_EGG2_k41.transcripts.sorted_fasta
#s1 = read_fasta('XENLA_cDNA_raw.v2.sorted_fasta')
#s2 = read_fasta('XENLA_cDNA_ref.v1.sorted_fasta')
#XENTR_cDNA_raw.v2.sorted_fasta
#XENTR_cDNA_ref.v1.sorted_fasta
seq = read_fasta(filename_fa)

for cls_id in clusters.keys():
    size = 1
    pct_id = 100.0
    if( clusters_stat.has_key(cls_id) ):
        size = clusters_stat[cls_id]['size']
        pct_id = clusters_stat[cls_id]['pct_id']

    if( seq.has_key(cls_id) ):
        print ">%s|%d|%.3f\n%s"%(cls_id,size,pct_id,''.join(seq[cls_id]))
    #elif( s2.has_key(cls_id) ):
    #    print ">%s|%d|%.3f\n%s"%(cls_id,size,pct_id,''.join(s2[cls_id]))
