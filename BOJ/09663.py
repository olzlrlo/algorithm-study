n = int(input())
queen = [0] * n


def dfs(row):
    global n, queen
    count = 0

    if row == n:  # 모든 행에 퀸을 배치했을 경우
        return 1

    for col in range(n):  # 모든 열에 대해 탐색
        queen[row] = col  # row 행, col 열에 퀸 배치

        for x in range(row):  # 이전 행 확인
            if queen[x] == queen[row]:  # 이전 행과 같은 열에 배치했을 경우
                break
            if abs(queen[x] - queen[row]) == abs(x - row):  # 이전 행의 대각선에 배치했을 경우
                break
        else:
            count += dfs(row + 1)  # 모든 열을 확인했다면 다음 행에 배치

    return count


print(dfs(0))  # 0행부터 채움
