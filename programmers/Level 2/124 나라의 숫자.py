def under_four(n):  # 3 이하의 수는 계산 생략
    if n == 1:
        return "1"
    elif n == 2:
        return "2"
    else:
        return "4"


def calculate(n):
    s = ''
    while n >= 3:  # 3진법처럼 계산
        if n % 3:
            s += str(n % 3)
            n //= 3
        else:  # 나머지가 0일 경우 4를 표시 (n = 몫 - 1)
            s += "4"
            n //= 3
            n -= 1
    s += str(n)
    return s[::-1]


def solution(n):
    if n <= 3:
        return under_four(n)
    else:
        answer = calculate(n)
        if '0' in answer:  # 0이 남아있을 경우 처리
            return answer[1:]
        else:
            return answer