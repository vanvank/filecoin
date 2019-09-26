#!/bin/bash

WALLET_ADDR=`go-filecoin address ls`
MESSAGE_CID=`curl -X POST -F "target=${WALLET_ADDR}" "http://user.kittyhawk.wtf:9797/tap" | cut -d" " -f4`
