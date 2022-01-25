n = int(input())
weight = []
for _ in range(n):
    weight.append(list(map(int, input().split())))


def travel(start, visited, total):
    if len(visited) == n:
        if weight[start][visited[0]]:
            global min_val
            total += weight[start][visited[0]]
            min_val = min(min_val, total)
        return

    for i in range(n):
        if i not in visited and weight[start][i]:
            visited.append(i)
            travel(i, visited, total + weight[start][i])
            visited.pop()


min_val = 10**9
for v in range(n):
    travel(v, [v], 0)

print(min_val)