#!/bin/bash
for HIT in $(ls *tnHit)
do
  echo $HIT
  ./tnHit-to-tnSite.py $HIT taagagtcag
done
