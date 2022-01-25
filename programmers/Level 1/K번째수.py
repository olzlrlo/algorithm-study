def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        cut = sorted(array[i - 1: j])
        answer.append(cut[k - 1])

    return answer
