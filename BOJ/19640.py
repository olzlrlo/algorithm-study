import sys
import heapq

input = sys.stdin.readline
n, m, k = map(int, input().split())
info = [[] for _ in range(m)]

for i in range(n):
    d, h = map(int, input().split())
    info[i % m].append((-d, -h, i))

while(True):
    compare = []
    for i in info:
        compare.append(i[0])
    print(compare)

    -d, -h, i = heapq.heappop(compare)
    print(d)
    break
