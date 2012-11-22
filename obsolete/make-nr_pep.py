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

pep_list = dict()
pep_h = ''
f_pep = open('%s_pep.fa'%data_name,'r')
for line in f_pep:
    if( line.startswith('>') ):
        pep_h = line.strip().lstrip('>')
        pep_list[pep_h] = []
    else:
        pep_list[pep_h].append( line.strip() )
f_pep.close()

pep_seq = dict()
for tmp_h in pep_list.keys():
    tmp_seq = ''.join(pep_list[tmp_h])
    if( not pep_seq.has_key(tmp_seq) ):
        pep_seq[tmp_seq] = []
    pep_seq[tmp_seq].append( tmp_h )

seq_idx = 1
f_cdna_out = open('%s_cdna_nr.fa'%data_name,'w')
f_pep_out = open('%s_pep_nr.fa'%data_name,'w')
f_cdna_raw = open('%s_cdna_nr.raw.fa'%data_name,'w')
f_pep_raw = open('%s_pep_nr.raw.fa'%data_name,'w')
for tmp_pseq in pep_seq.keys():
    longest_nseq = ''
    longest_h = ''
    for tmp_h in pep_seq[tmp_pseq]:
        tmp_nseq = ''.join(cdna_list[tmp_h])
        if( len(tmp_nseq) > len(longest_nseq) ):
            longest_h = tmp_h
            longest_nseq = tmp_nseq
    f_cdna_raw.write('>%s\n%s\n'%(longest_h,longest_nseq))
    f_pep_raw.write('>%s\n%s\n'%(longest_h,tmp_pseq))
    f_cdna_out.write('>%s_%08d\n%s\n'%(data_name,seq_idx,longest_nseq))
    f_pep_out.write('>%s_%08d\n%s\n'%(data_name,seq_idx,tmp_pseq))
    seq_idx += 1
f_pep_out.close()
f_cdna_out.close()
