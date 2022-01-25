# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= 1
    return result

# 재귀적으로 구현한 n!
# 점화식을 그대로 옮겨 반복문보다 간결함
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
