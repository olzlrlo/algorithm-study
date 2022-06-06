from collections import deque
n = int(input())
map_list = []
for _ in range(n):
    map_list.append(input())

answer = [0]


def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    dx, dy, depth = [0, 0, -1, 1], [-1, 1, 0, 0], 0
    while queue:
        x, y = queue.popleft()
        depth += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and map_list[nx][ny] == '1':
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return depth


visited = [[False] * n for _ in range(n)]
answer = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and map_list[i][j] == '1':
            result = bfs(i, j)
            answer.append(result)

print(len(answer))

for i in sorted(answer):
    print(i)