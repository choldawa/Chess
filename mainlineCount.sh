cat games/*.pgn | grep -I "^1." > lichess-raw.txt
sed -r -e 's/[0-9]*\.//g' -e 's#(0-1|1-0|1/2-1/2)##g' -e 's/\{[^\}]*\}//g' -e 's/[?!]+//g' -e 's/^[ ]*//g' -e 's/[ ]+/ /g' lichess-raw.txt > lichess.txt
inset=25
cut -d' ' -f1-$inset lichess.txt | sort | uniq -c | sed 's/^[ ]*//g' | tr -s ' ' > tmp-trunc-$inset.txt
while [ $inset -gt 0 ]
do
	outset=$(($inset - 1))
	echo $inset
	grep '^[ ]*[1-9] ' tmp-trunc-$inset.txt | tr -s ' ' | cut -d' ' -f1-$(($outset+1)) | sed 's/ /, /' > unique-$inset.txt
	grep -v '^[ ]*[1-9] ' tmp-trunc-$inset.txt >> tab-trunc.txt
	awk -F, '{sum[$2]+=$1}END{for(y in sum){print sum[y], y}}' unique-$inset.txt | tr -s ' ' > tmp-trunc-$outset.txt
	inset=$outset
done
