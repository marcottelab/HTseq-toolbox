#!/usr/bin/env python
import os
import sys
import re

filename_tnHit = sys.argv[1]
filename_out = re.sub(r'_tnHit$','',filename_tnHit)+'_tnSite'

rc = {'a':'t','t':'a','g':'c','c':'g','n':'n'}
def revcomp(tmp_seq):
    rv = []
    for tmp_n in tmp_seq[::-1]:
        rv.append(rc[tmp_n])
    return ''.join(rv)

#tn_f = 'taagagtcag'
#tn_r = 'ctgactctta'
tn_f = sys.argv[2].lower()
tn_r = revcomp(tn_f)

max_mismatch = 1

re_boundary_f = re.compile(r'([atgcn]{10,})([ATGCN]{10,})')
re_boundary_r = re.compile(r'([ATGCN]{10,})([atgcn]{10,})')

def calc_subs(tmp1,tmp2):
    if( len(tmp1) != len(tmp2) ):
        return -1
    return len([i for i in range(0,len(tmp1)) if tmp1[i] != tmp2[i]])

hit_counts = dict()
ins2reads = dict()
ins2edge_seq = dict()

count_perfect = 0
count_subs = 0
count_adjust = 0
count_no_hit = 0

f_log = open('%s.log'%filename_out,'w')
f_log.write('# TN_f: %s\n# TN_r: %s\n#max_mismatch=%d\n'%(tn_f,tn_r,max_mismatch))
f_tnHit = open(filename_tnHit,'r')
for line in f_tnHit:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    if( len(tokens) != 5 ):
        sys.stderr.write('Error:%s\n'%line.strip())
        continue
    tmp_id = tokens[0]
    tmp_strand = tokens[1]
    tmp_start = int(tokens[2])
    tmp_end = int(tokens[3])
    tmp_seq = tokens[4]

    if( not hit_counts.has_key(tmp_id) ):
        hit_counts[tmp_id] = 0
    hit_counts[tmp_id] += 1

    tmp_ins_site = -1
    tmp_edge_seq = ''
    if( tmp_strand == '+' ):
        tmp_ins_site = tmp_start
        re_edge = re.search(re_boundary_f,tmp_seq)
        if( re_edge == None ):
            count_no_hit += 1
            continue

        tmp_edge_tn = re_edge.group(1)[-10:]
        tmp_edge_g = re_edge.group(2)[:10]
        if( tmp_edge_tn == tn_f ):
            tmp_edge_seq = '%s%s'%(tmp_edge_tn,tmp_edge_g)
            count_perfect += 1
        elif( calc_subs(tmp_edge_tn, tn_f) <= max_mismatch ):
            f_log.write('%s\tsubs_matched\t%s\t%s.%s\n'%(tmp_id,tmp_strand,tmp_edge_tn,tmp_edge_g))
            tmp_edge_seq = '%s%s'%(tmp_edge_tn,tmp_edge_g)
            count_subs += 1
        else:
            for i in [1,2,3]:
                if( calc_subs(tmp_edge_tn[i:],tn_f[:-1*i]) <= max_mismatch and tmp_edge_g[0:i] == tn_f[-1*i:].upper() ):
                    tmp_ins_site += i
                    f_log.write('%s\tadjust_%d\t%s\t%s.%s ->'%(tmp_id,i,tmp_strand,tmp_edge_tn,tmp_edge_g))
                    tmp_edge_tn = '%s%s'%(tmp_edge_tn[i:],tmp_edge_g[0:i].lower())
                    tmp_edge_g = tmp_edge_g[i:]
                    f_log.write(' %s.%s\n'%(tmp_edge_tn,tmp_edge_g))
                    tmp_edge_seq = '%s%s'%(tmp_edge_tn,tmp_edge_g)
                    count_adjust += 1
                    break

    elif( tmp_strand == '-' ):
        tmp_ins_site = tmp_end
        tmp_edge = re.search(re_boundary_r,tmp_seq)
        re_edge = re.search(re_boundary_r,tmp_seq)
        if( re_edge == None ):
            count_no_hit += 1
            continue

        tmp_edge_g = re_edge.group(1)[-10:]
        tmp_edge_tn = re_edge.group(2)[:10]
        if( tmp_edge_tn == tn_r ):
            tmp_edge_seq = '%s%s'%(tmp_edge_g,tmp_edge_tn)
            count_perfect += 1
        elif( calc_subs(tmp_edge_tn, tn_r) <= max_mismatch ):
            f_log.write('%s\tsubs_matched\t%s\t%s\t%s\n'%(tmp_id,tmp_strand,tmp_edge_g,tmp_edge_tn))
            tmp_edge_seq = '%s%s'%(tmp_edge_g,tmp_edge_tn)
            count_subs += 1
        else:
            for i in [1,2,3]:
                if( calc_subs(tn_r[i:],tmp_edge_tn[:-1*i]) <= max_mismatch and tmp_edge_g[-1*i:] == tn_r[0:i].upper() ):
                    tmp_ins_site -= i
                    f_log.write('%s\tadjust_%d\t%s\t%s.%s ->'%(tmp_id,i,tmp_strand,tmp_edge_g,tmp_edge_tn))
                    tmp_edge_tn = '%s%s'%(tmp_edge_g[-1*i:].lower(),tmp_edge_tn[:-1*i])
                    tmp_edge_g = tmp_edge_g[:-1*i]
                    f_log.write(' %s.%s\n'%(tmp_edge_g,tmp_edge_tn))
                    count_adjust += 1
                    break
     
    if( tmp_edge_seq == '' ):
        count_no_hit += 1
        continue

    if( not ins2reads.has_key(tmp_ins_site) ):
        ins2reads[tmp_ins_site] = {'+':[], '-':[]}
    ins2reads[tmp_ins_site][tmp_strand].append(tmp_id)
f_tnHit.close()
count_total = count_perfect + count_subs + count_adjust + count_no_hit
f_log.write('# Total hits: %d\n'%count_total)
f_log.write('# Perfect edges: %d (%.2f pct)\n'%(count_perfect, count_perfect*100.0/count_total))
f_log.write('# Substituted edges: %d (%.2f pct)\n'%(count_subs, count_subs*100.0/count_total))
f_log.write('# Adjusted edges: %d (%.2f pct)\n'%(count_adjust, count_adjust*100.0/count_total))
f_log.write('# Errors: %d (%.2f pct)\n'%(count_no_hit, count_no_hit*100.0/count_total))
f_log.write('# Unique hits: %s\n'%(len([x for x in hit_counts.keys() if hit_counts[x] == 1])))
f_log.close()

f_out = open(filename_out,'w')
for tmp_ins_site in sorted(ins2reads.keys()):
    tmp_forward_reads = [x for x in ins2reads[tmp_ins_site]['+'] if hit_counts[x] == 1]
    tmp_reverse_reads = [x for x in ins2reads[tmp_ins_site]['-'] if hit_counts[x] == 1]
    f_out.write("%d\t%d\t%d\n"%(tmp_ins_site, len(tmp_forward_reads), len(tmp_reverse_reads)))
f_out.close()
