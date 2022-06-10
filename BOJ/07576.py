from collections import deque

m, n = map(int, input().split())
tomato = []
zero = 0
for i in range(n):
    tomato.append(list(map(int, input().split())))
    zero += tomato[i].count(0)

if not zero:
    print(0)
else:
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                queue.append((i, j, 0))

    while queue:
        x, y, depth = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not tomato[nx][ny]:
                zero -= 1
                tomato[nx][ny] = 1
                queue.append((nx, ny, depth + 1))

    if zero:
        print(-1)
    else:
        print(depth)