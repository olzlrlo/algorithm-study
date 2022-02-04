from collections import defaultdict


def dfs(start):
    visited[start] = True
    for v in networks[start]:
        if not visited[v]:
            dfs(v)


n_computer, n_network = int(input()), int(input())
networks = defaultdict(list)
for _ in range(n_network):
    c1, c2 = map(int, input().split())
    networks[c1].append(c2)
    networks[c2].append(c1)

visited = [False] * (n_computer + 1)
dfs(1)
print(visited.count(True) - 1)