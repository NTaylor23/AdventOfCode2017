#!/bin/bash

max_n=-1
result_file=""

for file in day0*a.py; do
    n=$(echo $file | grep -o -E '[0-9]+')
    if [[ $n -gt $max_n ]]; then
        max_n=$n
        result_file=$file
    fi
done

if [[ -z $result_file ]]; then
    echo "No matching file found."
else
    next_n=$((max_n + 1))
    next_filename_a=$(printf "day%02da.py" $next_n)
    next_filename_b=$(printf "day%02db.py" $next_n)
    touch $next_filename_a
    touch $next_filename_b
fi