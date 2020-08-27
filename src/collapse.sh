#!/bin/bash

infile=$1
inset=$2
mincount=$3
filename=tab-{$inset}-{$mincount}.txt

echo $filename

sed -e 's/ /,/' -e 's/[ ]+/ /g' $infile > tmpfile.txt
rm $filename
while [ $inset -gt 0 ]
do
	echo $inset
    cut -d' ' -f1-$(($inset)) tmpfile.txt | awk -F "," -v OFS="," '{sum[$2]+=$1}END{for(y in sum){print sum[y], y}}' > tmpfile.txt
    awk -F "," -v min="$mincount" '$1 >= min{print}' tmpfile.txt >> $filename
    awk -F "," -v min="$mincount" '$1 < min{print}' tmpfile.txt > tmpfile.txt
done
cat tmpfile.txt >> $filename
sed -i '' 's/,/ /' $filename
