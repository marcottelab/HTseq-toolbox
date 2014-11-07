#!/usr/bin/env python
import os
import sys
import h5py

## Script to convert Oxfort NanoPore fast5 to fastq
## Ref: https://gist.github.com/nickloman/3345d05e3a4642b5306c

fq_types = {'template' : '/Analyses/Basecall_2D_000/BaseCalled_template/Fastq',
            'complement' : '/Analyses/Basecall_2D_000/BaseCalled_complement/Fastq',
            'twodirections' : '/Analyses/Basecall_2D_000/BaseCalled_2D/Fastq'}

filename_f5 = sys.argv[1]

hdf5 = h5py.File(filename_f5,'r')
for tmp_type, tmp_path in fq_types.iteritems():
    try:
        fq_lines = hdf5[tmp_path][()].strip().split("\n")
        fq_lines[0] = "%s %s"%(fq_lines[0],tmp_type)
        print "\n".join(fq_lines)
    except Exception, e:
        pass
hdf5.close()
