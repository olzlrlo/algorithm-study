# 점화식: a_i = min(a_i-1, a_i/2, a_i/3, a_i/5) + 1
# 함수의 호출 횟수를 구하는 것이므로, 1씩 더해감

x = int(input())
d = [0] * (10**6 + 1) # DP 테이블

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1  # 1을 빼는 경우
    if not i % 2:  # 현재의 수가 2로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i//2] + 1)
    if not i % 3:  # 현재의 수가 3로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i//3] + 1)

print(d[x])
