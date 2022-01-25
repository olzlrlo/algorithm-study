import sys
from collections import deque

def bfs(start):
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited[node - 1] = True
        for n in graph[node - 1]:
            if not visited[n - 1]:
                queue.append(n)
                parents[n - 1].append(node)

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    graph[n1 - 1].append(n2)
    graph[n2 - 1].append(n1)

visited = [False] * n
parents = [[] for _ in range(n)]
bfs(1)

for parent in parents[1:]:
    print(parent[0])
