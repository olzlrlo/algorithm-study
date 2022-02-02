def sol():
    result, check = [], False
    dx, dy = (-1, 0, 1, 1, 1, 0, -1, -1), (-1, -1, -1, 0, 1, 1, 1, 0)
    for x, c_list in enumerate(clicked):
        tmp = ''
        for y, c in enumerate(c_list):
            if c == '.':  # 클릭 X
                tmp += '.'
            else:  # 클릭 O
                if grid[x][y] == '*':  # 폭탄일 경우
                    check = True
                    tmp += '*'
                else:  # 폭탄이 아닐 경우
                    bomb = 0
                    for i in range(8):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            if grid[nx][ny] == '*':
                                bomb += 1
                    tmp += str(bomb)
        result.append(tmp)

    return result, check


def check_bomb():
    bomb_list = []
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == '*':
                bomb_list.append((i, j))

    return bomb_list


n, grid, clicked = int(input()), [], []
for _ in range(n):
    grid.append(list(input()))
for _ in range(n):
    clicked.append(list(input()))

result, check = sol()
if check:  # 폭탄 열렸을 경우
    bomb_list = check_bomb()
    for x, y in check_bomb():
        result[x] = result[x][:y] + '*' + result[x][y+1:]

for x in result:
    print(x)
