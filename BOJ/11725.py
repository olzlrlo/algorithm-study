# DFS로 구현하면 재귀 때문에 메모리 초과

from collections import defaultdict
from collections import deque
import sys
read = sys.stdin.readline


def bfs(start):
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for i in adj[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                roots[i] += node


n, adj = int(read()), defaultdict(list)
for _ in range(n - 1):
    v1, v2 = map(int, read().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

roots = [0 for _ in range(n + 1)]
visited = [True, True] + [False] * (n - 1)
bfs(1)
for r in roots[2:]:
    print(r)