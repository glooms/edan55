import math
c = 0
print [(n, n * math.log(n)/2 - c * n) for n in [2**i - 1 for i in range(2, 21)]]
