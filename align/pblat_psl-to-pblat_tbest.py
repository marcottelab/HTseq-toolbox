#!/usr/bin/env python
import os
import sys
import gzip

data_name = sys.argv[1]

def get_species(tmp):
    for tmp_sp in ['HUMAN','MOUSE','XENTR','DANRE','CHICK']:
        if( tmp.find('.%s'%tmp_sp) > 0 ):
            return tmp_sp
    return 'UNKNOWN'

q2best = dict()
species_list = []
for filename in os.listdir('.'):
    if( not filename.startswith(data_name) ):
        continue
    if( not filename.endswith('.pblat_psl') and not filename.endswith('.pblat_psl.gz') ):
        continue

    f = open(filename,'r')
    if( filename.endswith('.gz') ):
        f = gzip.open(filename,'rb')
    tmp_species = get_species(filename)
    species_list.append(tmp_species)
    sys.stderr.write('Read %s (%s) ...'%(filename,tmp_species))
    for line in f:
        tokens = line.strip().split("\t")
        if( len(tokens) != 21 ):
            continue
        if( not tokens[0].isdigit() ):
            continue
        match = int(tokens[0])
        mismatch = int(tokens[1])
        q_gap_count = int(tokens[4])
        q_gap_bases = int(tokens[5])
        t_gap_count = int(tokens[6])
        t_gap_bases = int(tokens[7])
        strand = tokens[8]
        q_id = tokens[9]
        q_size = int(tokens[10])
        q_start = int(tokens[11])
        q_end = int(tokens[12])
        t_id = tokens[13]
        t_size = int(tokens[14])
        t_start = int(tokens[15])
        t_end = int(tokens[16])
        block_count = int(tokens[17])
        block_list = [x for x in tokens[18].rstrip(',').split(',')]
        qstart_list  = [x for x in tokens[19].rstrip(',').split(',')]
        tstart_list = [x for x in tokens[20].rstrip(',').split(',')]

        #q_ratio = (match - q_gap_bases)*100.0/q_size
        t_ratio = match*100.0/t_size
        tm_ratio = (match+mismatch)*100.0/t_size
        t_offset = abs(100.0 - t_ratio)

        if( not q2best.has_key(q_id) ):
            q2best[q_id] = dict()
        if( not q2best[q_id].has_key(tmp_species) ):
            q2best[q_id][tmp_species] = {'t_id':t_id, 'tm_ratio':tm_ratio, 't_ratio':t_ratio, 't_offset':t_offset}
        elif( q2best[q_id][tmp_species]['t_offset'] > t_offset ):
            q2best[q_id][tmp_species] = {'t_id':t_id, 'tm_ratio':tm_ratio, 't_ratio':t_ratio, 't_offset':t_offset}
    f.close()
    sys.stderr.write('  Done\n')

species_list = sorted(species_list)
f_out = open('%s.pblat_best'%data_name,'w')
f_out.write('SeqID\t%s\n'%( '\t'.join(species_list) ))
for tmp_q in sorted(q2best.keys()):
    out_str = []
    for tmp_sp in species_list:
        if( q2best[tmp_q].has_key(tmp_sp) ):
            tmp = q2best[tmp_q][tmp_sp]
            t_tokens = tmp['t_id'].split('|')
            out_str.append('%s|%s|%d|%d'%(t_tokens[0],t_tokens[3],int(tmp['t_ratio']),int(tmp['tm_ratio'])))
        else:
            out_str.append('NA')
    f_out.write('%s\t%s\n'%(tmp_q, '\t'.join(out_str)))
f_out.write('#target_name|target_id|coverage|identity\n')
f_out.close()
