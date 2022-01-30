from collections import deque


def bfs(start, words, target):
    queue = deque([(start, 0)])

    while queue:
        v, depth = queue.popleft()
        if v == target:
            return depth

        for word in words:
            cnt = 0
            for w1, w2 in zip(v, word):
                if w1 != w2:
                    cnt += 1
            if cnt == 1:
                queue.append((word, depth + 1))


def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        return bfs(begin, words, target)
