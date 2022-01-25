def dfs():
    if len(num_list) == m:
        print(*num_list)
        return

    for num in numbers:
            num_list.append(num)
            dfs()
            num_list.pop()

n, m = map(int, input().split())
numbers = [i + 1 for i in range(n)]
num_list = []
dfs()
