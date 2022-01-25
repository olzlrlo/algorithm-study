from collections import deque
n, l, r = map(int, input().split())
populations, result = [], 0
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
for _ in range(n):
    populations.append(list(map(int, input().split())))


def bfs(start, visited):
    queue = deque([start])
    total = 0
    connected = []

    while queue:
        x, y = queue.popleft()
        total += populations[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(populations[nx][ny] - populations[x][y]) <= r:
                    if not connected:
                        connected.append((x, y))
                    visited[nx][ny] = True
                    connected.append((nx, ny))
                    queue.append((nx, ny))

    if connected:
        for x, y in connected:
            populations[x][y] = total // len(connected)
        return True
    else:
        return False


check = True
while check:
    check = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                if bfs((i, j), visited):
                    check = True
    if check:
        result += 1

print(result)