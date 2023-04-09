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
    "day08a.py"
    "day08b.py"
    "day10a.py"
    "day10b.py"
    "day11a.py"
    "day11b.py"
    "day12a.py"
    "day12b.py"
    "day13a.py"
    "day14a.py"
    "day14b.py"
    "day15a.py"
    "day15b.py"
    "day16a.py"
    "day16b.py"
    "day17a.py"
    "day17b.py"
    "day18a.py"
    "day18b.py"
    "day19.py"
)

echo "/////////////// Advent Of Code 2017 ///////////////"
echo
for file in "${aoc_days[@]}"; do
    python3 "$file"
done
