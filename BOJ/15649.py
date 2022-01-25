# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 --> 순열
from itertools import permutations

n, m = map(int, input().split())
results = list(permutations([i for i in range(1, n + 1)], m))

for result in results:
    print(*result)
