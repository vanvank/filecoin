#!/bin/bash
DealID=$1
echo $(date) Begin watch $DealID Status
while true
do
    status=$(go-filecoin client query-storage-deal $DealID | awk '/Status/{print $2}')
    if [ "$status"x == "staged"x ]
    then
#       echo $status
        sleep 60
    elif [ "$status"x == "complete"x ]
    then
      echo $(date) $1 status change to $status
    break
    else
      echo $(date) $1 maybe something wrong occured
      break
    fi
done
