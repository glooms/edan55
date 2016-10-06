#!/bin/bash
rm out
for file in data/*.td
do
    python treewidth.py $file >> out
done
