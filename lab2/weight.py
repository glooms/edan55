import io
import sys

f = open(sys.argv[1], 'r')
f.readline();
weight_sum = 0;
for line in f :
    weight_sum += [int(i) for i in line.split()][2]
print weight_sum
