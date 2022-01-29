from collections import deque


def adjacent(word1, word2):
    cnt = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False


def bfs(start, words, target):
    queue = deque([(start, 1)])

    while queue:
        idx, depth = queue.popleft()
        if words[idx] == target:
            return depth
        for i, word in enumerate(words):
            if adjacent(words[idx], word):
                queue.append((i, depth + 1))


def solution(begin, target, words):
    if target not in words:
        return 0

    for i, word in enumerate(words):
        if adjacent(begin, word):
            return bfs(i, words, target)
