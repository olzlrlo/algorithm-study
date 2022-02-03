def check_BB():
    global BB
    BB += 1
    if t == BB and not word:
        return True
    return False


def check_DG():
    global DG
    DG += 1
    if t == DG and word:
        return True
    return False


a, t, word = int(input()), int(input()), int(input())

idx, rotate = 0, 2
BB, DG = 0, 0
while 1:
    if check_BB():  # 뻔
        print(idx%a)
        break
    idx += 1
    if check_DG():  # 데기
        print(idx%a)
        break
    idx += 1
    if check_BB():  # 뻔
        print(idx%a)
        break
    idx += 1
    if check_DG():  # 데기
        print(idx%a)
        break
    idx += 1
    for _ in range(rotate):
        if check_BB():
            print(idx%a)
            exit()
        idx += 1
    for _ in range(rotate):
        if check_DG():
            print(idx%a)
            exit()
        idx += 1
    rotate += 1


