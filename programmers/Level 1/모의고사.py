def solution(answers):
    answer = []
    memo = {1: 0, 2: 0, 3: 0} # 맞힌 개수 기록
    check1 = [1,2,3,4,5]
    check2 = [2,1,2,3,2,4,2,5]
    check3 = [3,3,1,1,2,2,4,4,5,5]

    for i, ans in enumerate(answers):
        if ans == check1[i % len(check1)]:
            memo[1] += 1
        if ans == check2[i % len(check2)]:
            memo[2] += 1
        if ans == check3[i % len(check3)]:
            memo[3] += 1

    max_val = max(memo.values())

    for key, val in memo.items():
        if max_val == val:
            answer.append(key)

    return answer
