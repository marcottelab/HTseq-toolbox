#!/usr/bin/python
import os
import sys
import gzip

filename_uc = sys.argv[1]
filename_db = sys.argv[2]
filename_fa = sys.argv[3]

clusters = dict()
clusters_stat = dict()

f_uc = open(filename_uc,'r')
if( filename_uc.endswith('.gz') ):
    f_uc = gzip.open(filename_uc,'rb')

for line in f_uc:
    if( line.startswith('S') ):
        tokens = line.strip().split("\t")
        if( not clusters.has_key( tokens[8] ) ):
            clusters[ tokens[8] ] = []
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

seq_db = read_fasta(filename_db)
seq_fa = read_fasta(filename_fa)

for db_id in seq_db.keys():
    if( not clusters.has_key(db_id) ):
        db_tokens = db_id.split('|')
        print ">%s|%s|%s|%s|NotAdded\n%s"%(db_tokens[0],db_tokens[1],db_tokens[2],db_tokens[3],''.join(seq_db[db_id]))

for cls_id in clusters.keys():
    size = 1
    pct_id = 100.0
    if( clusters_stat.has_key(cls_id) ):
        size = clusters_stat[cls_id]['size']
        pct_id = clusters_stat[cls_id]['pct_id']

    if( seq_db.has_key(cls_id) ):
        db_tokens = cls_id.split('|')
        prev_size = int(db_tokens[2])
        prev_pct_id = float(db_tokens[3])
        pct_id = (pct_id*size + prev_size*prev_pct_id)/(size+prev_size)
        size = size + prev_size
        print ">%s|%s|%d|%.3f\n%s"%(db_tokens[0],db_tokens[1],size,pct_id,''.join(seq_db[cls_id]))
    elif( seq_fa.has_key(cls_id) ):
        print ">%s|%d|%.3f\n%s"%(cls_id,size,pct_id,''.join(seq_fa[cls_id]))
