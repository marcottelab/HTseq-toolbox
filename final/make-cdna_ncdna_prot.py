#!/usr/bin/env python
import os
import sys

data_name = sys.argv[1]

def read_fasta(filename):
    rv = dict()
    tmp_h = ''
    f = open(filename,'r')
    for line in f:
        if( line.startswith('>') ):
            tmp_h = line.strip().lstrip('>')
            rv[tmp_h] = f.next().strip()
    f.close()
    return rv

filename_prot = '%s_NoPart_oTx_prot6.fa'%data_name
sys.stderr.write('Read %s ... '%filename_prot)
prot_seq = read_fasta('%s_NoPart_oTx_prot6.fa'%data_name)
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

rc = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
def revcomp(tmp_seq):
    return ''.join([rc[x] for x in tmp_seq[::-1]])

f_cdna = open('%s.cdna.fa'%data_name,'w')
f_err = open('%s.err.fa'%data_name,'w')
f_ncdna = open('%s.ncdna.fa'%data_name,'w')
f_ncdna_p = open('%s.ncdna_prot.fa'%data_name,'w')
f_prot = open('%s.prot.fa'%data_name,'w')

f_nseq = open('%s_NoPart_oTx.fa'%data_name,'r')
for line in f_nseq:
    if( line.startswith('>') ):
        tmp_h = line.strip().lstrip('>')
        tmp_seq = f_nseq.next().strip()
        if( unique_seq.has_key(tmp_h) ):
            f_prot.write('>p.%s\n%s\n'%(tmp_h,prot_seq['%s|%s'%(tmp_h,unique_seq[tmp_h])]))
            if( unique_seq[tmp_h].startswith('r') ):
                f_cdna.write('>c.%s\n%s\n'%(tmp_h,revcomp(tmp_seq)))
            else:
                f_cdna.write('>c.%s\n%s\n'%(tmp_h,tmp_seq))
        elif( dubious_seq.has_key(tmp_h) ):
            f_err.write('>e.%s\n%s\n'%(tmp_h,tmp_seq))
        else:
            tmp_prot_seq = ''
            for tmp_frame in ['f0','f1','f2','r0','r1','r2']:
                tmp_prot_id = '%s|%s'%(tmp_h,tmp_frame)
                if( not prot_seq.has_key(tmp_prot_id) ):
                    continue
                
                if( len(prot_seq[tmp_prot_id]) > len(tmp_prot_seq) ):
                    tmp_prot_seq = prot_seq[tmp_prot_id]
            f_ncdna.write('>nc.%s\n%s\n'%(tmp_h,tmp_seq))
            f_ncdna_p.write('>ncp.%s\n%s\n'%(tmp_h,tmp_prot_seq))

f_nseq.close()
