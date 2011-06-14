#!/bin/bash
for SAM_GZ in $(ls *sam.gz)
do
  echo $SAM_GZ
  DIRNAME=$(dirname $0)
  $DIRNAME/sam2sam_slim.py $SAM_GZ
done
