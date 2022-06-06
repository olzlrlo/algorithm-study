from collections import defaultdict

n, m = map(int, input().split())
friends = defaultdict(list)

for _ in range(m):
    f1, f2 = map(int, input().split())
    friends[f1].append(f2)
    friends[f2].append(f1)


def dfs(v, result):

    if len(result) == 5:
        global answer
        answer = 1
        return

    for friend in friends[v]:
        if friend not in result:
            dfs(friend, result+[friend])


global answer
answer = 0
for i in range(n):
    dfs(i, [i])
    if answer == 1:
        break

print(answer)
