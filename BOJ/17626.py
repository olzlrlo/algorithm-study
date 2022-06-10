import math
n = int(input())

if math.sqrt(n).is_integer():
    print(1)
else:
    dp = [0] * (n+1)  # defaultdict 시간 초과
    dp[1] = 1
    near = 1
    for i in range(2, n + 1):
        if math.sqrt(i).is_integer():
            dp[i] = 1
            near = i
        else:
            dp[i] = 10**10
            # 어떤 제곱 수랑 더할지 탐색
            for j in range(1, int(math.sqrt(near)) + 1):
                dp[i] = min(dp[i], dp[j**2] + dp[i-j**2])

    print(dp[n])
