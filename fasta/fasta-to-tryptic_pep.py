#!/usr/bin/python
import os
import sys
import re

filename_fa = sys.argv[1]

re_trypsin = re.compile('[KR]')
rc = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
min_len = 6

## http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG1
AAs    = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
Starts = '---M---------------M---------------M----------------------------'
Base1  = 'TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2  = 'TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
Base3  = 'TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
trans_tbl = dict()

for i in range(0,len(AAs)):
	trans_tbl['%s%s%s'%(Base1[i],Base2[i],Base3[i])] = AAs[i]

def translate(tmp_nseq):
	rv = []
	return ''.join([ trans_tbl[tmp_nseq[i:i+3]] for i in range(0,len(tmp_nseq)-2,3) ])

def revcomp(tmp_nseq):
    return ''.join([rc[x] for x in tmp_nseq.upper()[::-1]])
    
def trypsin_digest(pep_seq):
    rv = dict()
    
    pep_seq = pep_seq.split('*')[0]
    pos_cut = [tmp_m.start() for tmp_m in re_trypsin.finditer(pep_seq)]
    pos_cut.append(len(pep_seq))
    pos_init = 0
    for i_c0, pos_c0 in list(enumerate(pos_cut)):
        if( pos_c0 - pos_init > min_len ):
            rv["%d_C0"%pos_c0] = pep_seq[pos_init:pos_c0]

        i_c1 = i_c0 + 1
        if( i_c1 < len(pos_cut) ):
            pos_c1 = pos_cut[i_c1]
            if( pos_c1 - pos_init > min_len ):
                rv["%d_C1"%pos_c1] = pep_seq[pos_init:pos_c1]

        i_c2 = i_c0 + 2
        if( i_c2 < len(pos_cut) ):
            pos_c2 = pos_cut[i_c2]
            if( pos_c2 - pos_init > min_len ):
                rv["%d_C2"%pos_c2] = pep_seq[pos_init:pos_c2]
        pos_init = pos_c0

    return rv

h = ''
pep_idx = 0
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        h = line.strip()
        pep_idx = 0
    else:
        pep_idx += 1
        nseq = line.strip()
        for tmp_k,tmp_s in trypsin_digest(translate(nseq)).iteritems():
            print "%s_%s_F0\n%s"%(h,tmp_k,tmp_s)
            print tmp_s
        for tmp_k,tmp_s in trypsin_digest(translate(revcomp(nseq))).iteritems():
            print "%s_%s_F0rc\n%s"%(h,tmp_k,tmp_s)
            print tmp_s

        for tmp_k,tmp_s in trypsin_digest(translate(nseq[1:])).iteritems():
            print "%s_%s_F1\n%s"%(h,tmp_k,tmp_s)
            print tmp_s
        for tmp_k,tmp_s in trypsin_digest(translate(revcomp(nseq[1:]))).iteritems():
            print "%s_%s_F1rc\n%s"%(h,tmp_k,tmp_s)
            print tmp_s

        for tmp_k,tmp_s in trypsin_digest(translate(nseq[2:])).iteritems():
            print "%s_%s_F2\n%s"%(h,tmp_k,tmp_s)
            print tmp_s
        for tmp_k,tmp_s in trypsin_digest(translate(revcomp(nseq[2:]))).iteritems():
            print "%s_%s_F2rc\n%s"%(h,tmp_k,tmp_s)
            print tmp_s
f_fa.close()

