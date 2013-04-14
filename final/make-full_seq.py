#!/usr/bin/python
import os
import sys

data_name = sys.argv[1]
filename_prot = '%s.prot_final.fa'%data_name
filename_cdna = '%s.cdna_final.fa'%data_name

prot_seq = dict()
prot_h = dict()
f_prot = open(filename_prot,'r')
for line in f_prot:
    if( line.startswith('>') ):
        tmp_h = '.'.join(line.strip().lstrip('>').split('.')[1:])
        prot_seq[tmp_h] = f_prot.next().strip()
        prot_h[tmp_h] = line.strip().lstrip('>')
f_prot.close()

frame = dict()
f_frame = open('%s.unique_frame'%data_name,'r')
for line in f_frame:
    tokens = line.strip().split("\t")[0].split('|')
    frame[ '|'.join(tokens[:-1]) ] = int(tokens[-1][1])
f_frame.close()

def translate(tmp_nseq):
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

    rv = []
    for i in range(0,len(tmp_nseq)-2,3):
        tmp_codon = tmp_nseq[i:i+3]
        if( not trans_tbl.has_key(tmp_codon) ):
            rv.append('*')
        else:
            rv.append( trans_tbl[tmp_codon] )
    return ''.join(rv)

f_prot_full = open('%s.prot_full.fa'%data_name,'w')
f_cdna_full = open('%s.cdna_full.fa'%data_name,'w')
f_cds_full = open('%s.cds_full.fa'%data_name,'w')
f_prot_part = open('%s.prot_partial.fa'%data_name,'w')
f_cdna_part = open('%s.cdna_partial.fa'%data_name,'w')
f_cds_part = open('%s.cds_partial.fa'%data_name,'w')

count_full = 0
count_partial = 0

f_cdna = open(filename_cdna,'r')
for line in f_cdna:
    if( line.startswith('>') ):
        tmp_h = line.strip().lstrip('>')
        tmp_h_common = '.'.join(tmp_h.split('.')[1:])
        tmp_nseq = f_cdna.next().strip()

        if( not prot_seq.has_key(tmp_h_common) ):
            continue
        if( not frame.has_key(tmp_h_common) ):
            continue

        tmp_pseq = prot_seq[tmp_h_common]
        tmp_trans_seq = translate(tmp_nseq[frame[tmp_h_common]:])
        tmp_start = tmp_trans_seq.find(tmp_pseq)
        if( tmp_start < 0 ):
            sys.stderr.write("Error:%s\n"%tmp_h_common)
        
        stop_split = tmp_trans_seq.split('*')
        if( len(stop_split) == 1 or not tmp_pseq.startswith('M') ):
            count_partial += 1
            f_prot_part.write('>%s\n%s\n'%(prot_h[tmp_h_common], tmp_pseq))
            f_cdna_part.write('>%s\n%s\n'%(tmp_h, tmp_nseq))
            f_cds_part.write('>cds.%s\n%s\n'%(tmp_h_common, tmp_nseq[frame[tmp_h_common]+3*tmp_start:]))
            continue

        tmp_idx = 0
        for tmp_p in stop_split:
            if( tmp_p.find(tmp_pseq) >= 0 ):
                break
            tmp_idx += 1

        if( tmp_idx < len(stop_split) ):
            count_full += 1
            f_prot_full.write('>%s\n%s\n'%(prot_h[tmp_h_common], tmp_pseq))
            f_cdna_full.write('>%s\n%s\n'%(tmp_h, tmp_nseq))
            f_cds_full.write('>cds.%s\n%s\n'%(tmp_h_common, tmp_nseq[frame[tmp_h_common]+3*tmp_start:len(tmp_pseq)*3+3]))
            #print "Good: ",tmp_start, tmp_idx, len(stop_split)
        #tmp_cds = get_cds(tmp_f0, tmp_nseq)
f_cdna.close()

sys.stderr.write("%s - Full: %d, Partial %d\n"%(data_name, count_full, count_partial))
