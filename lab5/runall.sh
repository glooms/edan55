#!/bin/bash
rm out
for i in {1..20}
do
for file in data/*.td
do
    echo $file + ' ' + $i
    python treewidth.py $file $i >> out
done
done
