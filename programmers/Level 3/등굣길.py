from collections import deque


def solution(m, n, puddles):
    m, n = n, m  # 문제 오류
    answer = 0
    map = [[0] * (m + 1) for _ in range(n + 1)]
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    for x, y in puddles:
        map[x][y] = -1

    map[1][1] = 1
    queue = deque([(1, 1)])

    while queue:
        x, y = queue.popleft()
        rx, ry, dx, dy = x + 1, y, x, y + 1
        if 0 < rx <= n and 0 < ry <= m and map[rx][ry] != -1:  # 오른쪽으로 이동
            map[rx][ry] += map[x][y]  # 경우의 수 ++
            if not visited[rx][ry]:
                queue.append((rx, ry))
                visited[rx][ry] = True
        if 0 < dx <= n and 0 < dy <= m and map[dx][dy] != -1:  # 아래쪽으로 이동
            map[dx][dy] += map[x][y]  # 경우의 수 ++
            if not visited[dx][dy]:
                queue.append((dx, dy))
                visited[dx][dy] = True

    return map[n][m] % 1000000007