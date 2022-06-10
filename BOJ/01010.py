t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if n == 0:
        print(0)
        continue

    answer = 1

    for i in range(m, m-n, -1):
        answer *= i

    for i in range(1, n+1):
        answer //= i   # 부동 소수점 때문에 / 대신 //를 써야함

    print(int(answer))