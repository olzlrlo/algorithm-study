from functools import cmp_to_key


def comparator(a, b):
    if int(a + b) > int(b + a):
        return -1
    else:
        return 1


def solution(numbers):
    answer = ''
    numbers = [str(n) for n in numbers]
    numbers.sort(key=cmp_to_key(comparator))

    for s in numbers:
        answer += s

    return str(int(answer)) # 000 -> 0 위해 str(int())