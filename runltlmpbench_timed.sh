#!/bin/bash
echo "Hello World!, this is ltlmp benchmark test!"

while IFS= read -r line
do
	#echo "org: " $line
	#echo "mod: " "${line/'#'/}"
	if [ "$line" = "${line/'#'/}" ]
	then
		echo '--------------------- Round ---------------------------'
		python ./ltlmpsat.py -f "$line" > ./bench_result/log.txt &
		cmd_pid=$!
		sleep 3
		kill $cmd_pid
		python ./ltlmpsat.py -t -f "$line" > ./bench_result/log_t.txt &
		cmd_pid=$!
		sleep 3
		kill $cmd_pid
	else
		echo $line
	fi
done < "./bench/ltlmp_bench"