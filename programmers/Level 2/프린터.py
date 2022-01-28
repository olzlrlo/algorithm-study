from collections import deque


def solution(priorities, location):
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((p, i))

    answer = 1
    while True:
        max_val = max(priorities)
        for _ in range(len(queue)):
            priority, index = queue.popleft()
            if priority != max_val:
                queue.append((priority, index))
                continue
            else:  # 중요도 가장 높은 문서일 경우
                if location == index:  # 내가 요청한 문서일 경우
                    return answer
                else:
                    answer += 1
                    priorities[index] = -1
                    break

    return answer