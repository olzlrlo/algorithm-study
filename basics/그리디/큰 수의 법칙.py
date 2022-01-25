n, m, k = map(int, input().split) # 배열의 크기, 숫자가 더해지는 횟수, 연속 허용 횟수
nums = list(map(int, input().split))
result = 0

nums.sort()
first = nums[-1]
second = nums[-2]
remainder = m % (k + 1) # 나머지가 0이면 일괄 계산 가능

if first == second:
    result = first * m
else:
    result = first * k + second # 반복되는 수열의 합
    result *= m // (k + 1) # 몫만큼 곱함
    if remainder: # 나머지가 0이 아닐 경우
        result += first * remainder # 나머지만큼 곱한 후 더함

print(result)
