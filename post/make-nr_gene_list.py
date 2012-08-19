#!/usr/bin/env python
import os
import sys

data_name = sys.argv[1]

species_list = ['XENLA','HUMAN','XENTR','MOUSE','DANRE','CHICK','CAEEL','DROME']
if( len(sys.argv) > 2 ):
    species_list = [ sys.argv[2] ]

seq2ortho = dict()
for tmp_sp in species_list:
    t_summary = '%s_ens66_pep_longest.%s.bp+_summary'%(tmp_sp,data_name)
    q_summary = '%s.%s_ens66_pep_longest.bp+_summary'%(data_name,tmp_sp)
    if( tmp_sp == 'XENLA' ):
        t_summary = '%s_prot_v4.%s.bp+_summary'%(tmp_sp,data_name)
        q_summary = '%s.%s_prot_v4.bp+_summary'%(data_name,tmp_sp)
    
    f_t = open(t_summary,'r')
    for line in f_t:
        tokens = line.strip().split("\t")
        seq_list = tokens[1].split(',')
        for tmp_id in seq_list:
            if( not seq2ortho.has_key(tmp_id) ):
                seq2ortho[tmp_id] = dict()
            if( not seq2ortho[tmp_id].has_key(tmp_sp) ):
                seq2ortho[tmp_id][tmp_sp] = {'t':[],'q':[]}
            seq2ortho[tmp_id][tmp_sp]['t'].append( tokens[0] )
    f_t.close()
    
    f_q = open(q_summary,'r')
    for line in f_q:
        tokens = line.strip().split("\t")
        tmp_id = tokens[0]
        tgene_list = tokens[1].split(',')
        for tmp_tid in tgene_list:
            if( not seq2ortho.has_key(tmp_id) ):
                seq2ortho[tmp_id] = dict()
            if( not seq2ortho[tmp_id].has_key(tmp_sp) ):
                seq2ortho[tmp_id][tmp_sp] = {'t':[],'q':[]}
            seq2ortho[tmp_id][tmp_sp]['q'].append( tmp_tid )
    f_t.close()

for tmp_id in sorted(seq2ortho.keys()):
    for tmp_sp in species_list:
        if( not seq2ortho[tmp_id].has_key(tmp_sp) ):
            continue
        tmp_q = seq2ortho[tmp_id][tmp_sp]['q']
        tmp_t = seq2ortho[tmp_id][tmp_sp]['t']
        if( len(tmp_q) == 0 or len(tmp_t) == 0):
            continue
        tmp_overlap = [x for x in list(set(tmp_q).intersection(set(tmp_t))) if not x.startswith('unnamed')]

        if( len(tmp_overlap) == 0 ):
            continue
        print "%s\t%s\t%s"%(tmp_id,tmp_sp,','.join(sorted(tmp_overlap)))
        break

