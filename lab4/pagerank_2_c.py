import re
import sys

if len(sys.argv) != 3:
    sys.exit()

f = open(sys.argv[1], 'r')
r = int(sys.argv[2])
n = int(f.readline())
P = [[0] * n for _ in range(n)]
alpha = 0.85

def matrix_mul(A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_power(A, x):
    if x == 1:
        return A
    if x & 1:
        return matrix_mul(A, matrix_power(matrix_mul(A, A), x / 2))
    return matrix_power(matrix_mul(A, A), x / 2)

for line in f:
    s = [int(i) for i in re.findall(r'\d+', line)]
    for i in range(0, len(s), 2):
        P[s[i]][s[i + 1]] += 1

for i in xrange(len(P)):
    s = sum(P[i])
    if s != 0:
        P[i] = map(lambda x: alpha * float(x) / s  + (1-alpha) / n, P[i]) 
    else:
        P[i] = [float(1)/n] * n

P = matrix_power(P, r)

print P[0]
