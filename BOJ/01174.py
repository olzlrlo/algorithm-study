from itertools import combinations

n = int(input())
num = [i for i in range(10)]
cnt, idx = 1, 1  # 숫자 개수, 수 번호
flag = True

while flag:
    numbers = []
    for i in list(combinations(num, cnt)):
        s = ''
        for j in i[::-1]:
            s += str(j)
        numbers.append(s)

    if not numbers:
        print(-1)
        break
    for x in sorted(numbers):
        if idx == n:
            flag = False
            print(x)
            break
        idx += 1
    cnt += 1
