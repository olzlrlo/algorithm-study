n = int(input())
plans = input().split()

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D'] # 왼쪽, 오른쪽, 위, 아래

for plan in plans:
    # 이동 후 좌표
    for i in range(len(moves)):
        if plan == moves[i]:
            nx, ny = x + dx[i], y + dy[i]
    # 벗어나는지 확인
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    else:
        x, y = nx, ny

print(x, y)
