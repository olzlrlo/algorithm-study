import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        second = heapq.heappop(scoville)
        new_food = first + second * 2
        heapq.heappush(scoville, new_food)
        answer += 1

        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
            break

    return answer