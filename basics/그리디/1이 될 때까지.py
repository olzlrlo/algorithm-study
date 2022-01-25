n, k = map(int, input.split())
result = 0

while n >= k: # n이 k 이상일 때
    remainder = n % k
    if remainder: # 나머지만큼 빼기
        n -= remainder
        result += remainder
    n //= k # n을 k로 나누기
    result += 1

# 마지막으로 남은 수를 1까지 빼기
result += (n - 1)

print(result)
