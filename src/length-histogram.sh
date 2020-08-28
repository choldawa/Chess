#!/bin/bash

# count length distribution

awk '{print $1, gsub(/ /, "")}' $1 | awk '{++count[$2]; sum[$2]+=$1}END{for(y in count){print y, count[y], sum[y]}}' | sort -n