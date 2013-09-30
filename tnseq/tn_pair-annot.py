#!/usr/bin/env python
import os
import sys
import re

filename_tn_pair = sys.argv[1]

rc = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
def revcomp(tmp_seq):
    rv = []
    for tmp_n in tmp_seq[::-1]:
        rv.append(rc[tmp_n])
    return ''.join(rv)

read_len = 101
min_full_cov_len = 0.9 * read_len

tn_IR = 'GGATTCATCAG'
tn_IR_rc = revcomp(tn_IR)
tn_IR_len = len(tn_IR)

re_M = re.compile('\d+M')
re_endM = re.compile('\d+M$')
re_startM = re.compile('^\d+M')
def get_startM_endM(tmp_cigar):
    tmp_start = re_startM.search(tmp_cigar)
    if( tmp_start == None ):
        tmp_start = -1
    else:
        tmp_start = int(tmp_start.group(0).rstrip('M'))

    tmp_end = re_endM.search(tmp_cigar)
    if( tmp_end == None ):
        tmp_end = -1
    else:
        tmp_end = int(tmp_end.group(0).rstrip('M'))

    return tmp_start, tmp_end, sum([int(x.rstrip('M')) for x in re_M.findall(tmp_cigar)])

def check_Tn_IR(tmp_seq):
    if( tmp_seq == '.' ):
        return -1

    tmp_seq_no_sep = tmp_seq.replace('.','')
    if( tmp_seq_no_sep.find(tn_IR) >= 0 ):
        return tmp_seq_no_sep.find(tn_IR)
    if( tmp_seq_no_sep.find(tn_IR_rc) >= 0 ):
        return tmp_seq_no_sep.find(tn_IR_rc)

    max_match = 0
    max_pos = 0
    for i in range(0,len(tmp_seq_no_sep)-tn_IR_len):
        tmp_match = 0
        tmp_match_rc = 0
        for j in range(0,tn_IR_len):
            if(tmp_seq_no_sep[i+j] == tn_IR[j]):
                tmp_match += 1
            if(tmp_seq_no_sep[i+j] == tn_IR_rc[j]):
                tmp_match_rc += 1
        if( tmp_match > max_match ):
            max_match = tmp_match
            max_pos = i
        if( tmp_match_rc > max_match ):
            max_match = tmp_match_rc
            max_pos = i

    if( tn_IR_len - max_match < 2 ):
        return max_pos
    return -1

f_tn_pair = open(filename_tn_pair,'r')

f_gdna = open('%s_gdna'%filename_tn_pair,'w')
f_in = open('%s_in'%filename_tn_pair,'w')
f_unknown = open('%s_unknown'%filename_tn_pair,'w')
f_multi = open('%s_multi'%filename_tn_pair,'w')
for line in f_tn_pair:
    if( line.startswith('#') ):
        continue
    tmp_line = line.strip()
    tokens = tmp_line.split("\t")
    pair_id = tokens[0]

    tag1_list = tokens[2].split(';;')
    tag2_list = tokens[3].split(';;')

    if( len(tag1_list) == 1 and len(tag2_list) == 1 ):
        tag1_tokens = tag1_list[0].split('|')
        tag2_tokens = tag2_list[0].split('|')
        tag1_pos = int(tag1_tokens[0])
        tag2_pos = int(tag2_tokens[0])
        tmp1_startM, tmp1_endM, tmp1_sumM = get_startM_endM(tag1_tokens[2])
        tmp2_startM, tmp2_endM, tmp2_sumM = get_startM_endM(tag2_tokens[2])

        tn_pos1 = check_Tn_IR(tag1_tokens[3])
        tn_pos2 = check_Tn_IR(tag2_tokens[3])
        frag_len = max([ len(x) for x in tag1_tokens[3].split('.')] + [len(x) for x in tag2_tokens[3].split('.')])
        if( tn_pos1 >= 0 ):
            #if( tn_pos1 == frag_len-tn_IR_len or tn_pos1 == frag_len ):
            if( tag1_tokens[3][tn_pos1+tn_IR_len] == '.' ):
                f_in.write('%s\n'%tmp_line)
            elif( tmp1_startM > 0 ):
                tmp_diff = tn_pos1-frag_len
                f_in.write('%s\t%s\t%d|%s|%s|%s+%d\t%s\n'%(tokens[0],tokens[1],tag1_pos+tmp1_startM+tmp_diff,tag1_tokens[1],tag1_tokens[2],tag1_tokens[3],tmp_diff,tokens[3]))
            elif( tmp1_endM > 0 ):
                tmp_diff = tn_pos1-frag_len+tn_IR_len
                f_in.write('%s\t%s\t%d|%s|%s|%s+%d\t%s\n'%(tokens[0],tokens[1],tag1_pos+tmp_diff,tag1_tokens[1],tag1_tokens[2],tag1_tokens[3],tmp_diff,tokens[3]))
            else:
                print "Error"

        elif( check_Tn_IR(tag2_tokens[3]) >= 0 ):
            #if( tn_pos2 == frag_len-tn_IR_len or tn_pos2 == frag_len ):
            if( tag2_tokens[3][tn_pos2+tn_IR_len] == '.' ):
                f_in.write('%s\t%s\t%s\t%s\n'%(tokens[0],tokens[1],tokens[3],tokens[2]))
            elif( tmp2_startM > 0 ):
                tmp_diff = tn_pos2-frag_len
                f_in.write('%s\t%s\t%d|%s|%s|%s+%d\t%s\n'%(tokens[0],tokens[1],tag2_pos+tmp2_startM+tmp_diff,tag2_tokens[1],tag2_tokens[2],tag2_tokens[3],tmp_diff,tokens[2]))
            elif( tmp2_endM > 0 ):
                tmp_diff = tn_pos2-frag_len+tn_IR_len
                f_in.write('%s\t%s\t%d|%s|%s|%s+%d\t%s\n'%(tokens[0],tokens[1],tag2_pos+tmp_diff,tag2_tokens[1],tag2_tokens[2],tag2_tokens[3],tmp_diff,tokens[2]))
            else:
                print "Error"
        else:
            if( tmp1_sumM > min_full_cov_len ):
                if( tmp2_sumM > min_full_cov_len ):
                    ## Both reads are derived from genome, not Tn
                    f_gdna.write('%s\n'%tmp_line)
                else:
                    f_unknown.write('%s\n'%tmp_line)
            else:
                ## Ambiguous hit
                f_unknown.write('%s\n'%tmp_line)
    else:
        f_multi.write('%s\n'%tmp_line)
f_tn_pair.close()

f_gdna.close()
f_in.close()
f_unknown.close()
f_multi.close()
