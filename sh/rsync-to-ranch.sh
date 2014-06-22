#!/bin/bash

BACKUP_HOST=$RANCH_ID
BACKUP_ROOT=$HOME"/"$1

CMD="rsync -avz -e ssh $PWD $BACKUP_HOST:$BACKUP_ROOT"

date >> rsync-to-ranch.log
echo $CMD >> rsync-to-ranch.log
$CMD | tee -a rsync-to-ranch.log

