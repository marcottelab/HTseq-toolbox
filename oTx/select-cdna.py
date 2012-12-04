#!/usr/bin/python
import os
import sys

filename_oTx = sys.argv[1]
filename_prot = sys.argv[2]
data_name = filename_oTx.split('.')[0]

f_pout = open('%s_prot.fa'%data_name,'w')
f_cout = open('%s_cdna.fa'%data_name,'w')
f_ncout = open('%s_ncdna.fa'%data_name,'w')
f_names = open('%s_names.txt'%data_name,'w')

seq_h = ''
seq_list = dict()
f_oTx = open(filename_oTx,'r')
for line in f_oTx:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append(line.strip())
f_oTx.close()

rc = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
def revcomp(tmp_seq):
    return ''.join([rc[x] for x in tmp_seq[::-1]])

c_idx = 1
cdna_list = []
f_prot = open(filename_prot,'r')
for line in f_prot:
    if( line.startswith('>') ):
        h_prot = line.strip().lstrip('>')
        h_tokens = h_prot.split('|')
        h_oTx = h_tokens[0]
        cdna_list.append(h_oTx)
        seq_oTx = ''.join(seq_list[h_oTx])
        if( h_tokens[1].startswith('r') ):
            seq_oTx = revcomp(seq_oTx)
        f_cout.write('>c.%s_%09d\n%s\n'%(data_name,c_idx,seq_oTx))
        f_pout.write('>p.%s_%09d\n'%(data_name,c_idx))
        f_names.write('coding\t%s_%09d\t%s\t%s\n'%(data_name,c_idx,h_oTx,h_prot))
        c_idx += 1
    else:
        f_pout.write('%s\n'%(line.strip()))
f_prot.close()

for ncdna_id in sorted(list(set(seq_list.keys()) - set(cdna_list))):
    f_ncout.write('>nc.%s_%09d\n%s\n'%(data_name,c_idx, ''.join(seq_list[ncdna_id])))
    f_names.write('noncoding\t%s_%09d\t%s\n'%(data_name,c_idx,ncdna_id))

f_pout.close()
f_cout.close()
f_ncout.close()
f_names.close()
