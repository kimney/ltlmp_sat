#!/bin/bash
echo "Hello World!, this is ltlmp benchmark test!"

while IFS= read -r line
do
	#echo "org: " $line
	#echo "mod: " "${line/'#'/}"
	if [ "$line" = "${line/'#'/}" ]
	then
		echo "sharpnotfound!"
		python ./ltlmpsat.py -f "$line"
		python ./ltlmpsat.py -t -f "$line"
		python ./ltlmpsat.py -l -f "$line"
	fi
done < "./tests/ltlmp_bench"