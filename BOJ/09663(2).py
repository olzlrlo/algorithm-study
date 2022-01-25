n = int(input())
total = 0


def dfs(x, queen):
    if len(queen) == n:
        global total
        total += 1
        return

    for y in range(n):
        if y not in queen:
            for i, q in enumerate(queen):
                if x == i or y == q or abs(x - i) == abs(y - q):
                    break
            else:
                queen.append(y)
                dfs(x + 1, queen)
                queen.pop()


dfs(0, [])
print(total)

