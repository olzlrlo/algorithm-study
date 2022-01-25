def solution(brown, yellow):
    answer = []
    check = (brown - 4) // 2 # 꼭짓점 제외, 가로와 세로만 고려

    for i in range(check):
        if i * (check - i) == yellow:
            answer.append(check - i + 2)
            answer.append(i + 2)
            break

    return answer
