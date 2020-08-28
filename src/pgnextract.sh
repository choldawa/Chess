#!/bin/bash

for f in pgn/*.pgn;
do
    base=`basename $f .pgn`
    grep "^1." $f | sed -E -e 's/[0-9]*\.//g' -e 's#(0-1|1-0|1/2-1/2)##g' -e 's/\{[^}]*\}//g' -e 's/[?!]+//g' -e 's/^[ ]*//g' -e 's/[ ]+/ /g' > games/$base.txt
done
#cat games/*.pgn | grep "^1." | sed -E -e 's/[0-9]*\.//g' -e 's#(0-1|1-0|1/2-1/2)##g' -e 's/\{[^}]*\}//g' -e 's/[?!]+//g' -e 's/^[ ]*//g' -e 's/[ ]+/ /g' > $1
