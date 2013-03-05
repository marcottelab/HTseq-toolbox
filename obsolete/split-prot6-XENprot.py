#!/usr/bin/env python
import os
import sys

data_name = sys.argv[1]

filename_fa = ''
hit_list = dict()
for filename in os.listdir('.'):
    if( not filename.startswith(data_name) ):
        continue
    sys.stderr.write('%s\n'%filename)

    if( filename.endswith('.fa') ):
        filename_fa = filename
    
    if( filename.endswith('_best') ):
        f = open(filename,'r')
        for line in f:
            tokens = line.strip().split("\t")
            prot_id = tokens[0]
            cdna_id = prot_id.split('|')[0]
            if( not hit_list.has_key(cdna_id) ):
                hit_list[cdna_id] = []
            hit_list[cdna_id].append(prot_id)
        f.close()

count_single = 0
count_multi = 0

unique_hit_list = dict()
for tmp_cdna_id in sorted(hit_list.keys()):
    tmp_prot_list = list(set(hit_list[tmp_cdna_id]))
    if( len(tmp_prot_list) == 1 ):
        unique_hit_list[tmp_cdna_id] = tmp_prot_list[0]
        count_single += 1
    else:
        count_multi += 1

f_fa = open(filename_fa,'r')
f_XEN = open('%s_XENprot.fa'%(filename_fa.replace('_prot6.fa','')),'w')
f_noXEN = open('%s_noXENprot6.fa'%(filename_fa.replace('_prot6.fa','')),'w')
for line in f_fa:
    if( line.startswith('>') ):
        tmp_h = line.strip().lstrip('>')
        tmp_cdna_id = tmp_h.split('|')[0]
        if( unique_hit_list.has_key(tmp_cdna_id) ):
            if( tmp_h == unique_hit_list[tmp_cdna_id] ):
                tmp_flag = 1 
                f_XEN.write('>%s\n'%(tmp_h))
            else:
                tmp_flag = -1
        else:
            tmp_flag = 0
            f_noXEN.write('>%s\n'%(tmp_h))
    else:
        if( tmp_flag == 1 ):
            f_XEN.write('%s\n'%(line.strip()))
        elif( tmp_flag == 0 ):
            f_noXEN.write('%s\n'%(line.strip()))
f_noXEN.close()
f_XEN.close()
f_fa.close()
