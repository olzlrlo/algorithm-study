from collections import defaultdict


def solution(sticker):
    # 스티커가 하나만 있을 경우 예외 처리
    if len(sticker) == 1:
        return sticker[0]

    dp1, dp2 = defaultdict(int), defaultdict(int)

    dp1[0], dp1[1] = sticker[0], sticker[0]
    dp2[0], dp2[1] = 0, sticker[1]

    # 첫 번째 스티커 뗄 경우
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])

    # 첫 번째 스티커 안 뗄 경우
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])

    return max(max(dp1.values()), max(dp2.values()))