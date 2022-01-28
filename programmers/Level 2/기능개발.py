from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses, speeds = deque(progresses), deque(speeds)

    while progresses:
        for i, speed in enumerate(speeds):
            progresses[i] += speed

        cnt = 0
        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
            if not progresses:
                break
        if cnt:
            answer.append(cnt)

    return answer