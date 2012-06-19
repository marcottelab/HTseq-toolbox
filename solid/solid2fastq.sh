#!/bin/bash
## Script to run solid2fastq (from bfast) in a batch mode
for CSFASTA_GZ in $(ls *csfasta.gz)
do
  OUT=${CSFASTA_GZ%".csfasta.gz"}
  QUAL_GZ=$OUT"_QV.qual.gz"
  echo $OUT
  solid2fastq -z -Z -o $OUT $CSFASTA_GZ $QUAL_GZ
done
