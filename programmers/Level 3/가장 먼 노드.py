from collections import deque

def solution(n, edge):
    visited = [True] + [False] * (n - 1)
    max_depth, total = 0, 0

    graph = [[] for _ in range(n)]
    for n1, n2 in edge:
        graph[n1 - 1].append(n2)
        graph[n2 - 1].append(n1)

    # BFS
    queue = deque([(1, 0)])
    while queue:
        node, depth = queue.popleft()

        # 가장 멀리 떨어진 노드인지 확인
        if depth > max_depth:
            max_depth = depth
            total = 1
        elif depth == max_depth:
            total += 1

        # 인접 노드 탐색
        for adj in graph[node - 1]:
            if not visited[adj - 1]:
                visited[adj - 1] = True
                queue.append((adj, depth + 1))

    return total
