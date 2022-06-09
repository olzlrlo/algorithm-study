from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
indegree = defaultdict(int)
graph = defaultdict(list)

for _ in range(m):
    s1, s2 = map(int, input().split())
    graph[s1].append(s2)
    indegree[s2] += 1

queue = deque([])
for i in range(1, n + 1):
    if i not in indegree:
        queue.append(i)

result = []
while queue:
    node = queue.popleft()
    result.append(node)
    for adj in graph[node]:
        indegree[adj] -= 1
        if indegree[adj] == 0:
            queue.append(adj)

print(*result)