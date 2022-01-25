from functools import cmp_to_key

def comparator(a,b):
    if int(a + b) > int(b + a):
        return 1
    else: return -1

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key = cmp_to_key(comparator), reverse = True)
    answer = str(int(''.join(n))) # 리스트를 문자열로
    return answer
