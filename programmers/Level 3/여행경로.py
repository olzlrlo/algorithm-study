# 같은 항공권이 여러 개일 수 있음

from collections import defaultdict


def dfs(v, tickets, result):
    if not tickets:  # 항공권을 다 쓴 경우
        global answer
        answer.append(result)
        return

    global tickets_dict
    for t in tickets_dict[v]:
        print(tickets)
        if [v, t] in tickets:  # visited 대신 사용
            i = tickets.index([v, t])
            tickets.pop(i)
            dfs(t, tickets, result + [t])
            tickets.append([v, t])


def solution(tickets):
    global n_tickets
    n_tickets = len(tickets)

    global tickets_dict
    tickets_dict = defaultdict(list)

    for t1, t2 in tickets:
        tickets_dict[t1].append(t2)
    print(tickets_dict)

    for keys in tickets_dict.keys():  # 알파벳 순
        tickets_dict[keys].sort()

    global answer
    answer = []

    dfs('ICN', tickets, ['ICN'])

    return answer[0]