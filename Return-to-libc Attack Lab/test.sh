#!/bin/bash

echo "Starting scan (-200 a +200)..."

for i in $(seq -200 4 200); do
    if (( $i % 20 == 0 )); then
        echo "Testing offset: $i"
    fi
    python3 exploit_final.py $i
    ./retlib > output_temp.txt
done
