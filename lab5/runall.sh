#!/bin/bash
rm out
for file in data/*.td
do
    echo $file >> out
    python fast_iset.py $file >> out
    echo '' >> out
done
