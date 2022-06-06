from collections import defaultdict


def dfs(v, result):
    global total
    if len(result) == total:
        global answer
        answer.append(tuple(sorted(result)))
        return

    global mapping
    for id in mapping[len(result)]:
        if id not in result:
            dfs(id, result + [id])


def solution(user_id, banned_id):
    global answer
    answer = []

    global mapping
    mapping = defaultdict(list)

    global total
    total = len(banned_id)

    for i, bid in enumerate(banned_id):
        for j, uid in enumerate(user_id):
            if len(bid) == len(uid):
                for s1, s2 in zip(bid, uid):
                    if s1 == '*':
                        continue
                    elif s1 != s2:
                        break
                else:
                    mapping[i].append(j)

    for id in mapping[0]:
        dfs(id, [id])

    return len(set(answer))