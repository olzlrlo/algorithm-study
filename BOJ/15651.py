# 1부터 N까지 자연수 중에서 중복을 허용하여 M개를 고른 수열 --> 중복순열
from itertools import product

n, m = map(int, input().split())
results = list(product([i for i in range(1, n + 1)], repeat = m))

for result in results:
    print(*result)
