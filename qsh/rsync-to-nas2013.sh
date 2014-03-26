#!/bin/bash

BACKUP_HOST=$CYGNUS_ID
BACKUP_ROOT="/mnt/nas2013/"$1

CMD="rsync -avz -e ssh $PWD $BACKUP_HOST:$BACKUP_ROOT"
date >> rsync-to-nas2013.log
echo $CMD >> rsync-to-nas2013.log
$CMD | tee -a rsync-to-nas2013.log

