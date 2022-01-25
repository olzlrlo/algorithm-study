import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

answer = 0
for coin in coins[::-1]:
    if coin == k:
        answer += 1
        break
    elif coin < k:
        answer += (k // coin)
        k %= coin

print(answer)
