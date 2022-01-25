n, s = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0


def dfs(total, depth, cnt):
    if depth == n:
        if total == s and cnt > 0:
            global answer
            answer += 1
        return

    dfs(total + numbers[depth], depth + 1, cnt + 1)
    dfs(total, depth + 1, cnt)


dfs(0, 0, 0)
print(answer)