from collections import deque
from collections import defaultdict


def dfs(start):
    dfs_visited[start] = True
    global dfs_result
    dfs_result += (' ' + str(start))

    for i in adj[start]:
        if not dfs_visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    result = ''

    while queue:
        node = queue.popleft()
        result += (' ' + str(node))

        for i in adj[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return result


n, m, v = map(int, input().split())
adj = defaultdict(list)
for _ in range(m):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
    adj[v1].sort()
    adj[v2].sort()

dfs_visited, dfs_result = [False] * (n + 1), ''
dfs(v)
print(dfs_result[1:])

bfs_result = bfs(v)
print(bfs_result[1:])

