def dfs(v):
    if len(num_list) == m:
        print(*num_list)
        return

    for i in range(v, n):
        if numbers[i] not in num_list:
            num_list.append(numbers[i])
            dfs(i + 1)
            num_list.pop()

n, m = map(int, input().split())
numbers = [i + 1 for i in range(n)]
num_list = []
dfs(0)
