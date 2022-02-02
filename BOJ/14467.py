n = int(input())
total, moving = 0, [[] for _ in range(n + 1)]

for _ in range(n):
    idx, position = map(int, input().split())
    if not moving[idx]:
        moving[idx].append(position)
    elif position != moving[idx][-1]:
        moving[idx].append(position)

total = 0
for m in moving:
    if m:
        total += (len(m) - 1)


print(total)