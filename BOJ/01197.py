# Prim 알고리즘
# 현재 그래프에서 가장 짧은 간선을 골라 방문하지 않은 정점이라면 선택
import heapq
v, e = map(int, input().split())
graph, visited = [[] for _ in range(v + 1)], [False] * (v + 1)
for _ in range(e):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))
    graph[y].append((z, x))

heap = [[0, 1]]
answer, cnt = 0, 0
while heap:
    if cnt == v:  # v개 모두 방문하면 종료
        break
    weight, node = heapq.heappop(heap)
    if not visited[node]:  # node에 방문하지 않았을 경우
        visited[node] = True
        answer += weight
        cnt += 1
        for i in graph[node]:  # node와 연결된 다른 node를 heap에 넣음
            heapq.heappush(heap, i)

print(answer)