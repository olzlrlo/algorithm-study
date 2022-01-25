import sys
from itertools import permutations
input = sys.stdin.readline

n, k = map(int, input().split())
kits = list(map(int, input().split()))

answer = 0
results = list(permutations(kits, n))
for result in results:
    check, weight = True, 500
    for w in result:
        weight = weight - k + w
        if weight < 500:
            check = False
            break
    if check:
        answer += 1

print(answer)
