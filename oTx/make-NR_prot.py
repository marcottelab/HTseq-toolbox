#!/usr/bin/python
import os
import sys

data_name = sys.argv[1]

cdna_list = dict()
cdna_h = ''
f_cdna = open('%s_cdna.fa'%data_name,'r')
for line in f_cdna:
    if( line.startswith('>') ):
        cdna_h = line.strip().lstrip('>')
        cdna_list[cdna_h] = []
    else:
        cdna_list[cdna_h].append( line.strip() )
f_cdna.close()

prot_list = dict()
prot_h = ''
f_prot = open('%s_prot.fa'%data_name,'r')
for line in f_prot:
    if( line.startswith('>') ):
        prot_h = line.strip().lstrip('>')
        prot_list[prot_h] = []
    else:
        prot_list[prot_h].append( line.strip() )
f_prot.close()

prot_seq = dict()
for tmp_h in prot_list.keys():
    tmp_seq = ''.join(prot_list[tmp_h])
    if( not prot_seq.has_key(tmp_seq) ):
        prot_seq[tmp_seq] = []
    prot_seq[tmp_seq].append( tmp_h )

f_cdna_out = open('%s_cdna_NR.fa'%data_name,'w')
f_prot_out = open('%s_prot_NR.fa'%data_name,'w')
f_log_out = open('%s_NR.log'%data_name,'w')
for tmp_pseq in prot_seq.keys():
    longest_nseq = ''
    longest_h_prot = ''
    longest_h_cdna = ''
    for tmp_h in prot_seq[tmp_pseq]:
        tmp_h_cdna = tmp_h.replace('p.','c.')
        tmp_nseq = ''.join(cdna_list[tmp_h_cdna])
        if( len(tmp_nseq) > len(longest_nseq) ):
            longest_h_prot = tmp_h
            longest_h_cdna = tmp_h_cdna
            longest_nseq = tmp_nseq
    
    f_cdna_out.write('>%s\n%s\n'%(longest_h_cdna,longest_nseq))
    f_prot_out.write('>%s\n%s\n'%(longest_h_prot,tmp_pseq))
    f_log_out.write('%s\t%s\n'%(longest_h_prot, ';;'.join(prot_seq[tmp_pseq])))
f_prot_out.close()
f_cdna_out.close()
