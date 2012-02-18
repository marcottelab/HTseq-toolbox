#!/usr/bin/python
import os
import sys

## Criteria 
max_len = 10000
min_align_pct = 0.95
min_pct_id = 0.95
min_align_len = 0

filename_m9 = sys.argv[1]
filename_fa = sys.argv[2]

filename_base = filename_m9.replace('.self_megablast+_m9','')

seq_h = ''
seq_list = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append(line.strip())
f_fa.close()

seqlen = dict()
matched = dict()
f_m9 = open(filename_m9,'r')
for line in f_m9:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    query_id = tokens[0]
    target_id = tokens[1]
    pct_id = float(tokens[2])
    align_len = int(tokens[3])
    
    ## self hit: take seq length info then skip remaining part
    if( query_id == target_id ):
        if( not seqlen.has_key(query_id) ):
            seqlen[query_id] = align_len
        elif( seqlen[query_id] < align_len ):
            seqlen[query_id] = align_len
        continue

    if( not matched.has_key(query_id) ):
        matched[query_id] = []
    if( not matched.has_key(target_id) ):
        matched[target_id] = []
    
    ## collect hits based on min_pct_id and min_align_len
    if( pct_id > min_pct_id and align_len > min_align_len ):
        matched[query_id].append({'t':target_id,'id':pct_id,'len':align_len})
        matched[target_id].append({'t':query_id,'id':pct_id,'len':align_len})
f_m9.close()

#print "Total query seq:",len(seqlen.keys())
f_long = open('%s.cls_long.fa'%filename_base,'w')
f_single = open('%s.cls_single.fa'%filename_base,'w')
f_rep = open('%s.cls_rep.fa'%filename_base,'w')
f_member = open('%s.cls_member.fa'%filename_base,'w')

passed = dict()
for tmp_q in sorted(seqlen.keys(),key=seqlen.get,reverse=True):
    ## No hit
    if( not matched.has_key(tmp_q) ):
        passed[tmp_q] = -1
        f_single.write('>%s\n%s\n'%(tmp_q,''.join(seq_list[tmp_q])))
        continue
    
    ## handle seq longer than max_len (for efficient MUSCLE run)
    if( seqlen[tmp_q] > max_len ):
        passed[tmp_q] = -1
        f_long.write('>%s\n%s\n'%(tmp_q,''.join(seq_list[tmp_q])))
        continue
    
    ## skip seq assigned as members (or single/long)
    if( passed.has_key(tmp_q) ):
        continue

    target_list = []
    for tmp_m in matched[tmp_q]:
        tmp_t = tmp_m['t']
        if( passed.has_key(tmp_t) ):
            continue
        if( not seqlen.has_key(tmp_t) ):
            continue
        min_len = min(seqlen[tmp_q],seqlen[tmp_t])
        align_pct = float(tmp_m['len'])/min_len
        if( align_pct > min_align_pct ):
            target_list.append(tmp_t)
            passed[tmp_t] = 0
            f_member.write('>%s %s\n%s\n'%(tmp_t,tmp_q,''.join(seq_list[tmp_t])))

    ## if there's no meaningful target based on min_align_pct, treat it as single
    if( len(target_list) == 0 ):
        passed[tmp_q] = -1
        f_single.write('>%s\n%s\n'%(tmp_q,''.join(seq_list[tmp_q])))
        continue
    
    ## Write down the longest seq as rep.
    passed[tmp_q] = 1
    f_rep.write('>%s\n%s\n'%(tmp_q,''.join(seq_list[tmp_q])))

f_single.close()
f_rep.close()
f_member.close()
f_long.close()

#print "Clusters:",len([1 for x in passed.keys() if passed[x] == 1])
#print "Members :",len([1 for x in passed.keys() if passed[x] == 0])
#print "Singles :",len([1 for x in passed.keys() if passed[x] == -1])
