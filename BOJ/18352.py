from collections import defaultdict
from collections import deque

n, m, k, x = map(int, input().split())
road, distance = defaultdict(list), defaultdict(int)
for _ in range(m):
    c1, c2 = map(int, input().split())
    road[c1].append(c2)


def bfs(start, visited):
    queue = deque([(start, 1)])
    while queue:
        node, depth = queue.popleft()
        if not result[node]:
            result[node] = depth
        else:
            if result[node] > depth:
                result[node] = depth
        for i in road[node]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, depth + 1))


result = defaultdict(int)
for v in road[x]:
    visited = [False] * (n + 1)
    visited[x], visited[v] = True, True
    bfs(v, visited)

answer = []
for c in result:
    if result[c] == k:
        answer.append(c)

if not answer:
    print(-1)
else:
    answer.sort()
    for c in answer:
        print(c)



