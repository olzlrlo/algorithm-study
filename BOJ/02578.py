def check_row():
    line = 0
    for r in range(5):
        if not called[r].count(False):
            line += 1
    return line


def check_col():
    line = 0
    for r in range(5):
        cnt = 0
        for c in range(5):
            if not called[c][r]:
                cnt += 1
        if not cnt:
            line += 1
    return line


def check_cross():
    line, cnt = 0, 0
    for i in range(5):
        if not called[i][i]:
            cnt += 1
    if not cnt:
        line += 1
    cnt = 0
    for i in range(5):
        if not called[i][4 - i]:
            cnt += 1
    if not cnt:
        line += 1
    return line


def sol():
    for idx, num in enumerate(num_list):
        for r, b in enumerate(bingo):
            if num in b:
                c = b.index(num)
                called[r][c] = True
                if check_row() + check_col() + check_cross() >= 3:
                    print(idx + 1)
                    return


bingo, num_list, = [], []
for _ in range(5):
    bingo.append(list(map(int, input().split())))
for _ in range(5):
    num_list += list(map(int, input().split()))

called = [[False] * 5 for _ in range(5)]
sol()

