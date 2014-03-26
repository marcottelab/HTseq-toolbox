#!/bin/bash

BACKUP_HOST=$CYGNUS_ID
BACKUP_ROOT="/mnt/nas2012/"$1

CMD="rsync -avz -e ssh $PWD $BACKUP_HOST:$BACKUP_ROOT"
date >> rsync-to-nas2012.log
echo $CMD >> rsync-to-nas2012.log
$CMD | tee -a rsync-to-nas2012.log

