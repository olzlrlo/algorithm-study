from collections import defaultdict
import heapq

n, m = int(input()), int(input())
weights, connected = defaultdict(list), defaultdict(list)
for _ in range(m):
    c1, c2, w = map(int, input().split())
    weights[c1].append((w, c2))
    weights[c2].append((w, c1))

nodes = weights[1]
heapq.heapify(nodes)
visited = [False] * (n+1)
visited[1] = True
answer = 0
while nodes:
    weight, node = heapq.heappop(nodes)
    if visited[node]:
        continue
    answer += weight
    visited[node] = True
    for w, n in weights[node]:
        if not visited[n]:
            heapq.heappush(nodes, (w, n))

print(answer)