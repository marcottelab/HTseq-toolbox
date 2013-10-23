#!/usr/bin/env python
import os
import sys
import re

filename_pf_best = sys.argv[1]

re_DANRE_ofname = re.compile('\(\d+of\d\)')
re_MOUSE_gmname = re.compile('GM\d+$')
re_CxORFy = re.compile('C\d+ORF\d+$')

def is_named(tmp_name):
    if( tmp_name == 'NA' ):
        return -1
    if( len(tmp_name) > 10 ):
        return -1
    if( tmp_name.startswith('XB-') ):
        return -1
    if( tmp_name.startswith('SI_') ):
        return -1
    if( tmp_name.startswith('ZGC_') ):
        return -1
    if( tmp_name.endswith('RIK') ):
        return -1
    if( re_MOUSE_gmname.match(tmp_name) != None ):
        return -1
    if( re_CxORFy.match(tmp_name) != None ):
        return -1
    return 1

count_total = 0
count_unnamed = 0

count_perfect = 0
count_subname = 0
count_diffname = 0
count_no_target = 0
count_single_target = 0

count_multi_match = 0
count_multi_subname = 0
count_multi_diffname = 0
count_multi_no_win= 0

filename_base = filename_pf_best.replace('.prot_full_best','')

f_pf_best = open(filename_pf_best,'r')
f_out = open('%s.names'%filename_base,'w')
f_log = open('%s.names_log'%filename_base,'w')
for line in f_pf_best:
    tokens = line.strip().split("\t")

    count_total += 1
    q_name = '.'.join(tokens[0].split('|')[0].split('.')[1:]).upper()

    count_t = 0
    t_name_list = dict()
    for tmp_t in tokens[1:]:
        tmp_t_name = tmp_t.split('|')[0].upper()
        tmp_t_name = re_DANRE_ofname.sub('',tmp_t_name)
        if( is_named(tmp_t_name) < 0 ):
            continue
        if( not t_name_list.has_key(tmp_t_name) ):
            t_name_list[tmp_t_name] = 0
        t_name_list[tmp_t_name] += 1
        count_t += 1

    if( count_t  == 0 ):
        f_log.write("unnamed\t%s\tno_target\n"%(q_name))
        count_no_target += 1
    elif( count_t == 1 ):
        f_log.write("%s\t%s\tsingle_target\n"%(t_name_list.keys()[0],q_name))
        count_single_target += 1

    elif( len(t_name_list) == 1 ):
        t_name = t_name_list.keys()[0]
        f_log.write("%s\t%s\tperfect\n"%(t_name,q_name))
        f_out.write('%s\t%s\n'%(t_name,q_name))
    else:
        t_name_sorted = sorted(t_name_list.keys(),key=t_name_list.get)
        t_name_top = t_name_sorted[-1]
        if( t_name_list[t_name_top] > 1 ):
            f_log.write("%s\t%s\tmulti_best\n"%(';;'.join(t_name_sorted),q_name))
            f_out.write('%s\t%s\n'%(t_name_top,q_name))
        else:
            f_log.write("%s\t%s\tmulti_no_win\n"%(';;'.join(t_name_sorted),q_name))
            count_multi_no_win += 1
f_pf_best.close()
f_out.close()
f_log.close()
