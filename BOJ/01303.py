from collections import deque
from collections import defaultdict
n, m = map(int, input().split())
soldiers = []

for _ in range(m):
    soldiers.append(input())


def bfs(x, y, team):
    queue = deque([(x, y)])
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and soldiers[nx][ny] == team:
                if not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return cnt


visited = [[False] * n for _ in range(m)]
result = defaultdict(int)
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            power = bfs(i, j, soldiers[i][j])
            result[soldiers[i][j]] += (power ** 2)


print(result['W'], result['B'])