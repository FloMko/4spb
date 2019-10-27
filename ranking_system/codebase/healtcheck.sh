#!/usr/bin/env bash
echo Testing if $1 is UP

http_code=$(curl -LI $1 -o /dev/null -w '%{http_code}\n' -s)

if [ ${http_code} -eq 405 ]; then
    echo The service is UP and Running
    exit 0
else
    echo The service is DOWN
    exit 1
fi