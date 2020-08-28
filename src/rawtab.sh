#!/bin/bash

base=`basename $1 .txt`
cut -d ' ' -f1-$2 $1 | sort | uniq -c | sed -e 's/^[ ]*//g' -e 's/[ ]+/ /g' > tab/$base.tab
