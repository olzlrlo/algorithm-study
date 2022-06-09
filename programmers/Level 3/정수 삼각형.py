def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            tmp = []
            if j - 1 >= 0:
                tmp.append(triangle[i - 1][j - 1])
            if j <= i - 1:
                tmp.append(triangle[i - 1][j])

            triangle[i][j] += max(tmp)

    return max(triangle[-1])