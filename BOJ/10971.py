n = int(input())
weights = []
for i in range(n):
    weights.append(list(map(int, input().split())))


def dfs(v, w, depth, visited):
    global min_val, start
    if depth == n - 1 and weights[v][start]:
        min_val = min(min_val, w + weights[v][start])
        return

    visited[v] = True
    for i in range(n):
        if i != v and not visited[i] and weights[v][i]:
            dfs(i, w + weights[v][i], depth + 1, visited)
            visited[i] = False


min_val = 10**9
for start in range(n):
    dfs(start, 0, 0, [False] * n)

print(min_val)