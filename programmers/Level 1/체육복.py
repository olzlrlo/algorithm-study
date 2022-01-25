def solution(n, lost, reserve):
    answer = 0
    students = [1 for _ in range(n)] # 초기화

    for idx in lost:
        students[idx - 1] -= 1

    for idx in reserve:
        students[idx - 1] += 1

    for i in range(n):
        if students[i]: # 체육복이 있는 경우 continue
            continue
        elif i > 0 and students[i - 1] > 1: # 이전 번호 확인
            students[i] += 1
            students[i - 1] -= 1
        elif i < n - 1 and students[i + 1] > 1: # 다음 번호 확인
            students[i] += 1
            students[i + 1] -= 1

    answer = len([i for i in students if i])

    return answer
