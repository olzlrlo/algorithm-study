from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n+1)


def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        answer += 1
        bfs(i)

print(answer)