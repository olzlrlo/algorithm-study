from collections import deque


def solution(prices):
    answer = []

    queue = deque(prices)
    while queue:
        now_price = queue.popleft()
        cnt = 0
        for price in queue:
            if now_price <= price:
                cnt += 1
            elif queue:
                cnt += 1
                break
        answer.append(cnt)

    return answer