n = int(input())
target = int(input())

x, y, num = n//2, n//2, 1
result = [[0] * n for _ in range(n)]

result[x][y] = num
answer = (x, y)
rotate = 1

while rotate < n:

    for _ in range(rotate):  # 상
        x -= 1
        num += 1
        result[x][y] = num
        if num == target:
            answer = (x, y)

    for _ in range(rotate):  # 우
        y += 1
        num += 1
        result[x][y] = num
        if num == target:
            answer = (x, y)

    for _ in range(rotate + 1):  # 하
        x += 1
        num += 1
        result[x][y] = num
        if num == target:
            answer = (x, y)

    for _ in range(rotate + 1):  # 좌
        y -= 1
        num += 1
        result[x][y] = num
        if num == target:
            answer = (x, y)

    rotate += 2

for _ in range(rotate - 1):
    x -= 1
    num += 1
    result[x][y] = num
    if num == target:
        answer = (x, y)

ans_x, ans_y = answer
for i in result:
    for j in i[:-1]:
        print(j, end=' ')
    print(i[-1])
print(ans_x + 1, ans_y + 1)
