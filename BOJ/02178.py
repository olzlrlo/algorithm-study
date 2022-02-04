from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(input())


def bfs():
    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    while queue:
        def check(nx, ny):
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, depth + 1))

        x, y, depth = queue.popleft()
        if x == n - 1 and y == m - 1:
            return depth

        check(x, y + 1)  # 오른쪽
        check(x + 1, y)  # 아래쪽
        check(x - 1, y)  # 위쪽
        check(x, y - 1)  # 왼쪽


print(bfs())