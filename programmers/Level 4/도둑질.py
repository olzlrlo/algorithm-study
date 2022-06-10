# [1000, 1, 0, 1, 2, 1000, 0]
# 2001
from collections import defaultdict


def solution(money):
    dp1, dp2 = defaultdict(int), defaultdict(int)

    # 첫 번째 집 털 경우
    dp1[0], dp1[1] = money[0], money[0]
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫 번째 집 안 털 경우
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(max(dp1.values()), max(dp2.values()))