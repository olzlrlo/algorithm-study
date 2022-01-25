def solution(citations):
    n = range(len(citations) + 1) # 전체 논문 수

    for h in n[::-1]:
        more = [c for c in citations if c >= h] # h번 이상 인용된 논문
        if len(more) >= h: # h번 이상 인용된 논문이 h편 이상일 경우
            return h
