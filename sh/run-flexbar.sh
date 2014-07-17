#!/bin/bash

FLEXBAR="/work/taejoon/src.HTseq/flexbar/2.5/flexbar"
THREADS=1

for FQ in $(ls *fastq)
do
  TRIM_FQ=${FQ/.fastq/}".trimFB"
  if [ ! -e $TRIM_FQ".fastq" ]; then
    echo $FQ

    ## for version 2.5
    $FLEXBAR -f i1.8 -n $THREADS -ao 8 -m 15 -ae RIGHT -a ./3_adapter_seq.fa -r $FQ -t $TRIM_FQ

    ## for version 2.21
    #$FLEXBAR -f fastq-i1.8 -n $THREADS -ao 8 -m 15 -ae RIGHT -a $ADAPTER_FA -s $FQ -t $TRIM_FQ
  fi
done
