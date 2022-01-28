def solution1(brown, yellow):
    answer = []
    check = (brown - 4) // 2 # 꼭짓점 제외, 가로와 세로만 고려

    for i in range(check):
        if i * (check - i) == yellow:
            answer.append(check - i + 2)
            answer.append(i + 2)
            break

    return answer


def solution2(brown, yellow):
    answer = []
    sum = brown + yellow

    for i in range(3, sum // 2):
        if not sum % i:
            j = sum // i

            if yellow == (i - 2) * (j - 2):
                return [j, i]


def solution3(brown, yellow):
    answer = []

    for i in range(yellow):
        if not yellow % (i + 1):
            a, b = i + 1, yellow // (i + 1)
            if brown == 4 + (a * 2) + (b * 2):
                return [b + 2, a + 2]