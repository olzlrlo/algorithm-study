def dfs(v, visited, computers):
    visited[v] = True

    for i, connected in enumerate(computers[v]):
        if not visited[i] and connected:
            dfs(i, visited, computers)
    return


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            answer += 1

    return answe
