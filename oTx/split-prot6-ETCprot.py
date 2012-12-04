#!/usr/bin/env python
import os
import sys

data_name = sys.argv[1]

filename_fa = ''
hit_list = dict()
for filename in os.listdir('.'):
    if( not filename.startswith(data_name) ):
        continue

    if( filename.endswith('noXENprot6.fa') ):
        sys.stderr.write('%s\n'%filename)
        filename_fa = filename
    
    if( filename.endswith('_best') ):
        sys.stderr.write('%s\n'%filename)
        f = open(filename,'r')
        for line in f:
            if( line.startswith('#') ):
                continue
            tokens = line.strip().split("\t")
            prot_id = tokens[0]
            cdna_id = prot_id.split('|')[0]
            if( not hit_list.has_key(cdna_id) ):
                hit_list[cdna_id] = dict()
            hit_list[cdna_id][prot_id] = float(tokens[-1])
        f.close()

count_single = 0
count_multi = 0

unique_hit_list = dict()
best_hit_list = dict()
for tmp_cdna_id in sorted(hit_list.keys()):
    tmp_prot_list = list(set(hit_list[tmp_cdna_id].keys()))
    if( len(tmp_prot_list) == 1 ):
        unique_hit_list[tmp_cdna_id] = tmp_prot_list[0]
        count_single += 1
    else:
        tmp_prot_id = sorted(tmp_prot_list,key=hit_list[tmp_cdna_id].get)
        best_hit_list[tmp_cdna_id] = tmp_prot_id[-1]
        count_multi += 1

sys.stderr.write('Single:%d, Multi:%d\n'%(count_single, count_multi))

f_fa = open(filename_fa,'r')
f_ETC = open('%s_ETCprot.fa'%(filename_fa.replace('_noXENprot6.fa','')),'w')
f_noETC = open('%s_noETCprot6.fa'%(filename_fa.replace('_noXENprot6.fa','')),'w')
for line in f_fa:
    if( line.startswith('>') ):
        tmp_h = line.strip().lstrip('>')
        tmp_cdna_id = tmp_h.split('|')[0]
        if( unique_hit_list.has_key(tmp_cdna_id) ):
            if( tmp_h == unique_hit_list[tmp_cdna_id] ):
                tmp_flag = 1 
                f_ETC.write('>%s\n'%(tmp_h))
            else:
                tmp_flag = -1
        elif( best_hit_list.has_key(tmp_cdna_id) ):
            if( tmp_h == best_hit_list[tmp_cdna_id] ):
                tmp_flag = 1 
                f_ETC.write('>%s.m\n'%(tmp_h))
            else:
                tmp_flag = -1
        else:
            tmp_flag = 0
            f_noETC.write('>%s\n'%(tmp_h))
    else:
        if( tmp_flag == 1 ):
            f_ETC.write('%s\n'%(line.strip()))
        elif( tmp_flag == 0 ):
            f_noETC.write('%s\n'%(line.strip()))
f_noETC.close()
f_ETC.close()
f_fa.close()
