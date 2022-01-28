def solution1(citations):
    for h in range(len(citations) + 1)[::-1]:
        more = [c for c in citations if c >= h]
        if len(more) >= h:
            return h


def solution2(citations):
    for i in range(len(citations), -1, -1):
        cnt = 0
        for n in citations:
            if n >= i:
                cnt += 1
        if cnt >= i:
            return i