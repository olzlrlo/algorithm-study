from collections import deque

def dfs(start):
    print(start, end = ' ')
    visited1[start - 1] = True

    for n1, n2 in edges:
        if start == n1 and not visited1[n2 - 1]:
            visited1[n2 - 1] = True
            dfs(n2)
        if start == n2 and not visited1[n1 -1]:
            visited1[n1 - 1] = True
            dfs(n1)

def bfs(start):
    queue = deque([start])
    visited2[start - 1] = True

    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for n1, n2 in edges:
            if node == n1 and not visited2[n2 - 1]:
                visited2[n2 - 1] = True
                queue.append(n2)
            if node == n2 and not visited2[n1 - 1]:
                visited2[n1 - 1] = True
                queue.append(n1)
    print()

n, m, v = map(int, input().split())
edges = []

for _ in range(m):
    edge = list(map(int, input().split()))
    edges.append((min(edge), max(edge)))

edges.sort()
visited1, visited2 = [False] * n, [False] * n

dfs(v)
print()
bfs(v)
