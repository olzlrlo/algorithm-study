from collections import deque

def bfs(maps):
    m, n = len(maps[0]), len(maps)
    queue = deque([(0, 0, 1)])
    visited = [[-1] * m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited[0][0] = 1

    while queue:
        x, y, depth = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] and visited[nx][ny] < 0:
                    visited[nx][ny] = depth + 1
                    queue.append((nx, ny, depth + 1))

    return visited[-1][-1]


def solution(maps):
    return bfs(maps)