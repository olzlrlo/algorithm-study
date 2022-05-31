# 플로이드 워셜 알고리즘은 그래프가 adjacency matrix 형식으로 표현됐을 때 사용 가능

def solution(n, results):
    graph = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for winner, loser in results:
        graph[winner][loser] = True  # 이기면 True
        graph[loser][winner] = False  # 지면 False

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if graph[j][i] == None:
                    continue
                # j가 i에게, i가 k에게 졌다면 j는 k에게 짐
                # j가 i를, i가 k를 이겼다면 j가 k를 이김
                if graph[j][i] == graph[i][k]:
                    graph[j][k] = graph[j][i]
                    graph[k][j] = not graph[j][i]

    answer = 0
    for i in range(1, n + 1):
        # 자기 자신을 제외하고 True 혹은 False일 경우 순위 확정
        if None in graph[i][1:i] + graph[i][i + 1:]:
            continue
        answer += 1

    return answer