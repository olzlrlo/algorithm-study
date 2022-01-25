from collections import deque
n = int(input())
dx, dy, space = [0, -1, 1, 0], [-1, 0, 0, 1], []
shark, eat, time = 2, 0, 0  # 크기, 먹은 횟수
for _ in range(n):
    space.append(list(map(int, input().split())))


def bfs(now):
    queue, possible = deque([now]), []
    while queue:
        x, y, depth = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if 0 <= space[nx][ny] <= shark:  # 이동 가능: 빈칸, 크기가 작거나 같은 물고기
                    queue.append((nx, ny, depth + 1))
                if 0 < space[nx][ny] < shark:  # 먹기 가능: 크기가 작은 물고기
                    possible.append((depth + 1, nx, ny))
    if not possible:  # 먹을 수 있는 물고기가 없는 경우
        return False
    else:  # 먹을 수 있는 물고기가 있는 경우
        global eat, time
        eat += 1
        depth, x, y = sorted(possible)[0]  # 거리, 행, 열 순으로 정렬
        time += depth
        space[x][y] = 9
        return True


check = True
while check:
    check = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                visited[i][j] = True
                if bfs((i, j, 0)):
                    check = True
                    space[i][j] = 0  # 상어 자리 -> 빈칸
                    if shark == eat:  # 상어 크기만큼 먹었을 경우
                        shark += 1
                        eat = 0
            if check:
                break
        if check:
            break

print(time)