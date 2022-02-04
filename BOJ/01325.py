from collections import defaultdict
from collections import deque


def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    total = 0

    while queue:
        node = queue.popleft()
        for i in trust[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                total += 1
    return total


n, m = map(int, input().split())
trust = defaultdict(list)
for _ in range(m):
    c1, c2 = map(int, input().split())
    trust[c2].append(c1)

max_val, max_idx = 0, []
for i in range(1, n+1):
    result = bfs(i)
    if max_val < result:
        max_val, max_idx = result, [i]
    elif max_val == result:
        max_idx.append(i)

print(*max_idx)