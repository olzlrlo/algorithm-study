def dfs(start, computers, visited):
    visited[start] = True
    computer = computers[start]

    for i in range(len(computer)):
        if not visited[i] and computer[i] == 1:
            dfs(i, computers, visited)

    return

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            answer += 1

    return answer
