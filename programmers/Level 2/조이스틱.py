from itertools import product
from collections import deque


def solution(name):
    # 이름이 AAA... 일 경우
    if name.count('A') == len(name):
        return 0

    # 상하로 움직이는 최소 횟수
    answer = 0
    for s in name:
        answer += min(ord(s) - ord('A'), ord('Z') - ord(s) + 1)

    # 좌우로 움직이는 최소 횟수
    result = set()
    for moves in list(product((-1, 1), repeat=len(name) - 1)):  # 좌우 이동 모든 경우의 수
        name_deque = deque(name)
        default = deque('A' * len(name))
        for i, move in enumerate([0] + list(moves)):  # i = 0: 안 움직임
            # 좌 or 우로 움직인 후 상하로 조작했을 때
            name_deque.rotate(move)
            default.rotate(move)
            default[0] = name_deque[0]
            # 알파벳 이름이 완성될 경우
            if name_deque == default:
                result.add(i)
                break

    return answer + min(result)