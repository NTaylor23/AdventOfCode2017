#!/bin/bash

aoc_days=(
    "day01a.py"
    "day01b.py"
    "day02a.py"
    "day02b.py"
    "day03a.py"
    "day03b.py"
    "day04a.py"
    "day04b.py"
    "day05a.py"
    "day05b.py"
    "day06a.py"
    "day06b.py"
    "day07a.py"
)

echo "/////////////// Advent Of Code 2017 ///////////////"
echo
for file in "${aoc_days[@]}"; do
    python3 "$file"
done
