#!/bin/bash
TISSUE=$1
for FA in $(ls *$TISSUE*/transcripts.fa)
do
    NEW=${FA/\/transcripts.fa/.oTx.fa}
    echo "$FA --> $NEW"
    mv $FA $NEW
done
