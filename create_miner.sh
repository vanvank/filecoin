#!/bin/bash
go-filecoin miner create 100 --gas-price=0.001 --gas-limit=300 --peerid `go-filecoin id | jq -r '.ID'`
