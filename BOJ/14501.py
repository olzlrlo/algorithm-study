def dfs(now_t, now_p):
    if now_t >= n:
        global max_val
        max_val = max(now_p, max_val)
        return

    if now_t + time[now_t] <= n:  # 일을 하는 경우
        dfs(now_t + time[now_t], now_p + pay[now_t])

    dfs(now_t + 1, now_p)  # 일을 안 하고 넘어가는 경우


n = int(input())
time, pay = [], []
max_val = 0

for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

dfs(0, 0)
print(max_val)
