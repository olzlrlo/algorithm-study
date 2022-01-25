from collections import deque

def bfs():
    queue = deque([1])

    while queue:
        computer = queue.popleft()
        visited[computer - 1] = True
        for c1, c2 in networks:
            if computer == c1 and not visited[c2 - 1]:
                queue.append(c2)
            if computer == c2 and not visited[c1 - 1]:
                queue.append(c1)

n, m = int(input()), int(input())
networks = []
visited = [False] * n

for _ in range(m):
    c1, c2 = map(int, input().split())
    networks.append((c1, c2))

bfs()
print(visited.count(True) - 1)
