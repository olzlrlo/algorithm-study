def solution(N, number):
    answer = -1
    dp = [[]]

    for i in range(1, 9):  # N 개수
        result = set()
        result.add(int(str(N) * i))  # N, NN, NNN, ...

        for j in range(1, i):
            for r1 in dp[j]:  # j번 사용
                for r2 in dp[i - j]:  # i-j번 사용
                    result.add(r1 + r2)
                    result.add(r1 - r2)
                    result.add(r1 * r2)
                    if r2:
                        result.add(r1 / r2)

        if number in result:
            answer = i
            break

        dp.append(result)

    return answer