import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        second = heapq.heappop(scoville)
        new_food = first + 2 * second
        answer += 1
        heapq.heappush(scoville, new_food)

        if len(scoville) == 1:
            break

    if scoville[0] >= K:
        return answer
    else:
        return -1