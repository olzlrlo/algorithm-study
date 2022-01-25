# 금액 i를 만들 수 있는 최소한의 화폐 개수를 a_i, 화폐의 단위를 k라고 했을 때
# a_i-k = min(a_i, a_i-k + 1) or 10001(방법 없음)

n, m = map(int, input().split())  # n가지 종류의 화폐로 m원을 만들어야 함
coins = []
for _ in range(n):
    coins.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0  # 0원은 화페를 사용하지 않아도 만들 수 있음

for coin in coins:  # 모든 화폐에 대해 반복
    for i in range(coin, m + 1):  # 각 coin부터 m원까지 확인
            d[i] = min(d[i], d[i - coin] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
