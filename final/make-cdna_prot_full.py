#!/usr/bin/env python
import os
import sys

data_name = sys.argv[1]
min_plen = 11

filename_prot = '%s.prot.fa'%data_name
filename_cdna = '%s.cdna.fa'%data_name

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

start_codons = ['TTG','CTG','ATG']
def translate(tmp_nseq):
    ## http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG1
    AAs    = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts = '---M---------------M---------------M----------------------------'
    Base1  = 'TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
    Base2  = 'TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
    Base3  = 'TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
    trans_tbl = dict()

    for i in range(0,len(AAs)):
        trans_tbl['%s%s%s'%(Base1[i],Base2[i],Base3[i])] = AAs[i]

    rv = []
    for i in range(0,len(tmp_nseq)-2,3):
        tmp_codon = tmp_nseq[i:i+3]
        if( not trans_tbl.has_key(tmp_codon) ):
            rv.append('X')
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
            sys.stderr.write('No prot seq:%s\n'%tmp_h_common)
            continue
        if( not frame.has_key(tmp_h_common) ):
            sys.stderr.write('No frame:%s\n'%tmp_h_common)
            continue

        tmp_pseq = prot_seq[tmp_h_common]
        tmp_trans_pseq = translate(tmp_nseq[frame[tmp_h_common]:])

        if( tmp_trans_pseq.find(tmp_pseq) < 0 ):
            sys.stderr.write("Error:%s\n"%tmp_h_common)
            sys.exit(1)
        
        tmp_pstart_ppos = tmp_trans_pseq.index(tmp_pseq)
        tmp_pend_ppos = tmp_pstart_ppos + len(tmp_pseq)
        tmp_start_codon_npos = frame[tmp_h_common] + 3 * tmp_pstart_ppos

        with_start_codon = 0
        tmp_start_codon_ppos = 0

        for tmp_npos in range(tmp_start_codon_npos,len(tmp_nseq),3):
            tmp_codon = ''.join(tmp_nseq[tmp_npos:tmp_npos+3])
            if( tmp_codon in start_codons ):
                tmp_start_codon_npos = tmp_npos
                with_start_codon = 1
                break
            tmp_start_codon_ppos += 1

        if( with_start_codon == 0 ):
            ## No start codon
            count_partial += 1
            f_prot_part.write('>%s\n%s\n'%(prot_h[tmp_h_common], tmp_pseq))
            f_cdna_part.write('>%s\n%s\n'%(tmp_h, tmp_nseq))
            f_cds_part.write('>cds.%s\n%s\n'%(tmp_h_common, tmp_nseq[tmp_start_codon_npos:]))
            continue

        tmp_pseq = tmp_pseq[tmp_start_codon_ppos:]
        if( tmp_pseq.startswith('L') ):
            tmp_pseq = 'M%s'%tmp_pseq[1:]
        tmp_cds_seq = tmp_nseq[tmp_start_codon_npos:tmp_start_codon_npos+len(tmp_pseq)*3+3]
        
        if( tmp_trans_pseq.find('*') < 0 or tmp_pend_ppos == len(tmp_trans_pseq) ):
            ## No stop codon   
            count_partial += 1
            f_prot_part.write('>%s\n%s\n'%(prot_h[tmp_h_common], tmp_pseq))
            f_cdna_part.write('>%s\n%s\n'%(tmp_h, tmp_nseq))
            f_cds_part.write('>cds.%s\n%s\n'%(tmp_h_common, tmp_cds_seq))
            continue
        
        if( len(tmp_pseq) < min_plen ):
            ## Too short to be true
            count_partial += 1
            if( len(tmp_pseq) > 0 ):
                f_prot_part.write('>%s\n%s\n'%(prot_h[tmp_h_common], tmp_pseq))
            f_cdna_part.write('>%s\n%s\n'%(tmp_h, tmp_nseq))
            f_cds_part.write('>cds.%s\n%s\n'%(tmp_h_common, tmp_cds_seq))
            continue
 
        count_full += 1
        f_prot_full.write('>%s\n%s\n'%(prot_h[tmp_h_common], tmp_pseq))
        f_cdna_full.write('>%s\n%s\n'%(tmp_h, tmp_nseq))
        f_cds_full.write('>cds.%s\n%s\n'%(tmp_h_common, tmp_cds_seq))
f_cdna.close()

sys.stderr.write("%s - Full: %d, Partial %d\n"%(data_name, count_full, count_partial))
