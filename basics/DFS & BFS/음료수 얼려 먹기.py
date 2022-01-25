# DFS
n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드를 방문한 뒤, 인접 노드도 방문
def dfs(x, y):
    # 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        # 상하좌우 모두 탐색
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
