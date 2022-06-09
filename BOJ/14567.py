from collections import defaultdict
from collections import deque


n, m = map(int, input().split())
subjects = defaultdict(list)
indegree = defaultdict(int)

for _ in range(m):
    s1, s2 = map(int, input().split())
    subjects[s1].append(s2)
    indegree[s2] += 1

queue = deque([])
result = [0] * n
for i in range(1, n+1):
    if i not in indegree:
        queue.append((i, 1))

while queue:
    node, depth = queue.popleft()
    result[node - 1] = depth
    for adj in subjects[node]:
        indegree[adj] -= 1
        if indegree[adj] == 0:
            queue.append((adj, depth+1))

print(*result)