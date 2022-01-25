# BFS, 너비 우선 탐색
# 가까운 노드부터 탐색하는 알고리즘
# Queue 자료구조 활용
# 일반적인 경우, 수행 시간은 DFS보다 좋음

# 1. 탐색 시작 노드를 큐에 삽입 후, 방문 처리
# 2. 큐에서 노드를 꺼내,
    # 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입 후 방문 처리
# 3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복
from collections import deque

def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True # 현재 노드 방문 처리

    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9

bfs(graph, 1, visited)
