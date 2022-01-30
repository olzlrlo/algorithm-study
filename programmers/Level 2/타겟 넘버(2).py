from itertools import product


def solution(numbers, target):
    answer = 0

    for xx in list(product((-1, 1), repeat=len(numbers))):
        sum = 0
        for x, number in zip(xx, numbers):
            sum += (x * number)
        if sum == target:
            answer += 1

    return answer