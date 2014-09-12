#!/bin/bash
echo "Hello World!, this is ltlmp benchmark test!"

while IFS= read -r line
do
	#echo "org: " $line
	#echo "mod: " "${line/'#'/}"
	if [ "$line" = "${line/'#'/}" ]
	then
		echo '--------------------- Round ---------------------------'
		python ./ltlmpsat.py -f "$line"
		python ./ltlmpsat.py -t -f "$line"
	else
		echo $line
	fi
done < "./bench/ltlmp_bench_heavy"