# 위상 정렬
from collections import deque
from collections import defaultdict

n = int(input())
before, after, indegree, time = defaultdict(list), defaultdict(list), defaultdict(int), defaultdict(int)
max_node = defaultdict(int)
start = []
for i in range(1, n+1):
    read = list(map(int, input().split()))
    time[i] = read[0]
    indegree[i] += read[1]
    for v in read[2:]:
        before[i].append(v)
        after[v].append(i)
    if not indegree[i]:
        start.append(i)

queue = deque(start)
while queue:
    node = queue.popleft()
    for adj in after[node]:
        indegree[adj] -= 1
        if indegree[adj] == 0:
            queue.append(adj)
            # 선행 노드 중, 가장 시간이 오래 걸린 노드 찾기
            max_node = before[adj][0]
            for v in before[adj]:
                if time[max_node] < time[v]:
                    max_node = v
            time[adj] += time[max_node]

else:
    print(max(time.values()))