#!/usr/bin/python
import os
import sys

data_name = sys.argv[1]

def read_seqlen(filename):
    rv = dict()
    tmp_h = ''
    f = open(filename,'r')
    for line in f:
        if( line.startswith('>') ):
            tmp_h = line.strip().lstrip('>')
            rv[tmp_h] = len(f.next().strip())
    f.close()
    return rv

filename_prot = '%s_NoPart_oTx_prot6.fa'%data_name
sys.stderr.write('Read %s ... '%filename_prot)
prot_len = read_seqlen('%s_NoPart_oTx_prot6.fa'%data_name)
sys.stderr.write('Done\n')

sys.stderr.write('Read frame ... ')
dubious_seq = dict()
f_dubious = open('%s.dubious_frame'%data_name,'r')
for line in f_dubious:
    tokens = line.strip().split("\t")
    dubious_seq[ tokens[0] ] = 1
f_dubious.close()

unique_seq = dict()
f_unique = open('%s.unique_frame'%data_name,'r')
for line in f_unique:
    tokens = line.strip().split("\t")
    prot_id = tokens[0]
    cdna_id = prot_id.split('|')[0]
    tmp_frame = prot_id.split('|')[1]
    unique_seq[cdna_id] = tmp_frame
f_unique.close()
sys.stderr.write('Done\n')

f_cdna = open('%s.cdna_len_dist'%data_name,'w')
f_ncdna = open('%s.ncdna_len_dist'%data_name,'w')

f_nseq = open('%s_NoPart_oTx.fa'%data_name,'r')
for line in f_nseq:
    if( line.startswith('>') ):
        tmp_h = line.strip().lstrip('>')
        tmp_seq = f_nseq.next().strip()
        if( dubious_seq.has_key(tmp_h) ):
            continue

        if( unique_seq.has_key(tmp_h) ):
            tmp_prot_len = prot_len[ '%s|%s'%(tmp_h,unique_seq[tmp_h]) ]
            f_cdna.write('%s\t%d\t%d\t%.3f\n'%(tmp_h,len(tmp_seq), tmp_prot_len, tmp_prot_len*3.0/len(tmp_seq) ))
        else:
            tmp_prot_len = 0
            for tmp_frame in ['f0','f1','f2','r0','r1','r2']:
                tmp_id = '%s|%s'%(tmp_h,tmp_frame)
                if( not prot_len.has_key(tmp_id) ):
                    continue
                
                if( prot_len[tmp_id] > tmp_prot_len ):
                    tmp_prot_len = prot_len[tmp_id]
            f_ncdna.write('%s\t%d\t%d\t%.3f\n'%(tmp_h,len(tmp_seq), tmp_prot_len, tmp_prot_len*3.0/len(tmp_seq) ))
f_nseq.close()
