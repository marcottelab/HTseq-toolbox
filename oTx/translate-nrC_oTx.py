#!/usr/bin/python
import os
import sys

data_name = sys.argv[1]

min_plen = 6

seq_list = dict()
seq_frame = dict()

for filename in os.listdir('.'):
    if( filename.find(data_name) < 0 ):
        continue
    #print filename

    if( filename.endswith('.fa') ):
        seq_h = ''
        f_fa = open(filename,'r')
        for line in f_fa:
            if( line.startswith('>') ):
                seq_h = line.strip().lstrip('>')
                seq_list[seq_h] = []
            else:
                seq_list[seq_h].append(line.strip())
        f_fa.close()

    if( filename.find('best_') >= 0 ):
        f_best = open(filename,'r')
        for line in f_best:
            tokens = line.strip().split("\t")
            seq_id = tokens[0]
            seq_start = int(tokens[3])
            seq_end = int(tokens[4])

            if( not seq_frame.has_key(seq_id) ):
                seq_frame[seq_id] = []
            seq_frame[seq_id].append( {'start':seq_start,'end':seq_end} )
        f_best.close()

## http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG1
AAs    = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
Starts = '---M---------------M---------------M----------------------------'
Base1  = 'TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2  = 'TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
Base3  = 'TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
rc = {'A':'T','T':'A','G':'C','C':'G','N':'N','M':'M','R':'R','S':'S','Y':'Y','D':'D','W':'W','K':'K','V':'V','B':'B'}
trans_tbl = dict()

for i in range(0,len(AAs)):
    trans_tbl['%s%s%s'%(Base1[i],Base2[i],Base3[i])] = AAs[i]
    #trans_tbl['CMC'] = 'P'  ## exception
    #trans_tbl['MCC'] = 'P'
    #trans_tbl['CCM'] = 'P'  

def translate(tmp_nseq):
    rv = []
    for i in range(0,len(tmp_nseq)-2,3):
        tmp_codon = tmp_nseq[i:i+3]
        if( not trans_tbl.has_key(tmp_codon) ):
            rv.append('*')
        else:
            rv.append( trans_tbl[tmp_codon] )
    return ''.join(rv)
	#return ''.join([ trans_tbl[tmp_nseq[i:i+3]] for i in range(0,len(tmp_nseq)-2,3) ])

def revcomp(tmp_nseq):
    return ''.join([rc[x] for x in tmp_nseq.upper()[::-1]])

f_pfa = open('%s_pep.fa'%data_name,'w')
f_nfa = open('%s_cdna.fa'%data_name,'w')

for tmp_h in sorted(seq_frame.keys()):
    tmp_nseq = ''.join(seq_list[tmp_h])
    tmp_len = len(tmp_nseq)
    count_sense = 0
    count_anti = 0
    count_frame_idx = {0:0, 1:0, 2:0}

    for tmp_frame in seq_frame[tmp_h]:
        tmp_start = tmp_frame['start']
        if( tmp_frame['start'] > tmp_frame['end'] ):
            count_anti += 1
            tmp_start = tmp_len - tmp_frame['start'] + 1
        else:
            count_sense += 1
    
        tmp_frame_idx = tmp_start % 3
        count_frame_idx[tmp_frame_idx] += 1
    
    max_frame_idx = sorted(count_frame_idx.keys(),key=count_frame_idx.get)[-1]

    if( count_anti > count_sense ):
        tmp_nseq = revcomp(tmp_nseq)
   
    max_frame_idx -= 1
    if( max_frame_idx < 0 ):
        max_frame_idx = 2

    tmp_pseq = translate(tmp_nseq[max_frame_idx:])
    longest_pep = ''

    for tmp_pep in tmp_pseq.split('*'):
        if( tmp_pep.find('M') < 0 ):
            continue

        tmp_p_start = tmp_pep.index('M')
        tmp_pep = tmp_pep[tmp_p_start:]

        if( len(tmp_pep) > len(longest_pep) ):
            longest_pep = tmp_pep
    
    if( len(longest_pep) < min_plen ):
        continue
    
    if( not longest_pep.startswith('M') ):
        print tmp_h
        print longest_pep
        print tmp_pseq
        print tmp_p_start
        sys.exit(1)

    # if( tmp_h.find('_6447_') >= 0 ):
    #     print tmp_h,max_frame_idx

    #if( count_sense+count_anti < 6 ):
    #    continue
    #print tmp_h,count_frame_idx,count_sense,count_anti
    #print tmp_pseq
    f_pfa.write('>%s\n%s\n'%(tmp_h,longest_pep))
    f_nfa.write('>%s\n%s\n'%(tmp_h,tmp_nseq))
f_pfa.close()
f_nfa.close()
