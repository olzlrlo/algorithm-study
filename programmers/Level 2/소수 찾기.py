from itertools import permutations


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True


def solution(numbers):
    answer = 0

    for i in range(len(numbers) + 1):
        num_sets = set(permutations(numbers, i + 1))
        for num_set in num_sets:
            num = ''
            if num_set[0] == '0':
                continue
            for s in num_set:
                num += s
            if isPrime(int(num)):
                answer += 1

    return answer