#!/bin/bash

cat games/*.pgn | grep "^1." | sed -E -e 's/[0-9]*\.//g' -e 's#(0-1|1-0|1/2-1/2)##g' -e 's/\{[^}]*\}//g' -e 's/[?!]+//g' -e 's/^[ ]*//g' -e 's/[ ]+/ /g' > $1
