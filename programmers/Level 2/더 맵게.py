import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        food1 = heapq.heappop(scoville)
        if food1 < K:  # 스코빌 지수가 K 미만인 음식이 있을 경우
            if scoville:  # 섞을 음식이 남아있을 경우
                food2 = heapq.heappop(scoville)
                new_food = food1 + 2 * food2
                heapq.heappush(scoville, new_food)
                answer += 1
            else:  # 섞을 음식이 없을 경우
                return -1
        else:  # 스코빌 지수가 K 미만인 음식이 없을 경우
            return answer