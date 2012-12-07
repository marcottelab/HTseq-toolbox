#!/usr/bin/python
import os
import sys
import gzip

filename_prot_fa = sys.argv[1]

filename_base = filename_prot_fa.replace('_prot_NR.fa','')
filename_part = '%s_prot_NR.self.bp+_tbl_part'%filename_base
filename_cdna_fa = '%s_cdna_NR.fa'%filename_base

prot_h = ''
prot_list = dict()
prot_len = dict()
f_fa = open(filename_prot_fa,'r')
if( filename_prot_fa.endswith('.gz') ):
    f_fa = gzip.open(filename_prot_fa,'rb')
for line in f_fa:
    if( line.startswith('>') ):
        prot_h = line.strip().lstrip('>')
        prot_list[prot_h] = []
        prot_len[prot_h] = 0
    else:
        prot_list[prot_h].append(line.strip())
        prot_len[prot_h] += len(line.strip())
f_fa.close()

cdna_h = ''
cdna_list = dict()
cdna_len = dict()
f_fa = open(filename_cdna_fa,'r')
if( filename_cdna_fa.endswith('.gz') ):
    f_fa = gzip.open(filename_cdna_fa,'rb')
for line in f_fa:
    if( line.startswith('>') ):
        cdna_h = line.strip().lstrip('>')
        cdna_list[cdna_h] = []
        cdna_len[cdna_h] = 0
    else:
        cdna_list[cdna_h].append(line.strip())
        cdna_len[cdna_h] += len(line.strip())
f_fa.close()

q2t = dict()
t2q = dict()
f_part = open(filename_part,'r')
for line in f_part:
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    q_len = int(tokens[1])
    t_id = tokens[2]
    t_len = int(tokens[3])
    if( not q2t.has_key(q_id) ):
        q2t[q_id] = dict()
    q2t[q_id][t_id] = 1
    if( not t2q.has_key(t_id) ):
        t2q[t_id] = dict()
    t2q[t_id][q_id] = 1
f_part.close()

is_part = dict()
for tmp_h in sorted(prot_len.keys(),key=prot_len.get,reverse=True):
    if( is_part.has_key(tmp_h) ):
        continue
    
    if( t2q.has_key(tmp_h) ):
        for tmp_q in t2q[tmp_h].keys():
            is_part[tmp_q] = 1

f_ncdna = open('%s_ncdna_extra.fa'%filename_base,'w')
f_log = open('%s_final.log'%filename_base,'w')
translate_failed = dict()
prot_map = dict()
for tmp_h in prot_list.keys():
    if( is_part.has_key(tmp_h) ):
        continue

    tmp_cdna_h = tmp_h.replace('p.','c.')
    tmp_cdna_seq = ''.join(cdna_list[tmp_cdna_h])

    tmp_seq = ''.join(prot_list[tmp_h])
    if( tmp_seq.find('M') < 0 ):
        translate_failed[tmp_h] = 1
        f_ncdna.write('>%s\n%s\n'%(tmp_cdna_h,tmp_cdna_seq))
        f_log.write('%s\tnoM\n'%tmp_h)
        continue

    tmp_posM = tmp_seq.index('M')
    tmp_Mseq = tmp_seq[tmp_posM:]
    if( len(tmp_Mseq) < 6 ):
        translate_failed[tmp_h] = 1
        f_ncdna.write('>%s\n%s\n'%(tmp_cdna_h,tmp_cdna_seq))
        f_log.write('%s\tshort_pep\n'%tmp_h)
        continue
    
    if( not prot_map.has_key(tmp_Mseq) ):
        prot_map[tmp_Mseq] = []
    prot_map[tmp_Mseq].append(tmp_h)
f_ncdna.close()

f_prot = open('%s_prot_final.fa'%filename_base,'w')
f_cdna = open('%s_cdna_final.fa'%filename_base,'w')
for tmp_pseq in prot_map.keys():
    h_good = []
    h_partial = []
    h_failed = []
    longest_prot_h = ''
    longest_cdna_h = ''
    longest_cdna_seq = ''
    for tmp_h in prot_map[tmp_pseq]:
        if( is_part.has_key(tmp_h) ):
            h_partial.append(tmp_h)
            continue

        h_good.append(tmp_h)
        tmp_cdna_h = tmp_h.replace('p.','c.')
        tmp_cdna_seq = ''.join(cdna_list[tmp_cdna_h])
        if( longest_cdna_h == '' ):
            longest_prot_h = tmp_h
            longest_cdna_h = tmp_cdna_h
            longest_cdna_seq = tmp_cdna_seq
        elif( len(longest_cdna_seq) < len(tmp_cdna_seq) ):
            longest_prot_h = tmp_h
            longest_cdna_h = tmp_cdna_h
            longest_cdna_seq = tmp_cdna_seq
    
    if( len(h_good) == 0 ):
        for tmp_h in prot_map[tmp_pseq]:
            tmp_cdna_h = tmp_h.replace('p.','c.')
            tmp_cdna_seq = ''.join(cdna_list[tmp_cdna_h])
            f_ncdna.write('>%s\n%s\n'%(tmp_cdna_h,tmp_cdna_seq))

    else:
        f_prot.write('>%s\n%s\n'%(longest_prot_h,tmp_pseq))
        f_cdna.write('>%s\n%s\n'%(longest_cdna_h,longest_cdna_seq))
        if( len(h_good) > 1 ):
            f_log.write('%s\tdup\t%s\n'%(longest_prot_h,':;'.join(h_good)))
        if( len(h_failed) > 0 ):
            f_log.write('%s\tTN_failed\t%s\n'%(longest_prot_h,':;'.join(h_failed)))
        if( len(h_partial) > 0 ):
            f_log.write('%s\tpartial\t%s\n'%(longest_prot_h,':;'.join(h_partial)))
f_cdna.close()
f_prot.close()
f_log.close()
