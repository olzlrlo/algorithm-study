import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

plus, minus, mul, div = ['+'] * opers[0], ['-'] * opers[1], ['*'] * opers[2], ['/'] * opers[3]
operator = plus + minus + mul + div
operators = list(permutations(operator, n - 1))

min, max = 10000000000000, -10000000000000
for operator in operators:
    sum = nums[0]
    for num, op in zip(nums[1:], operator):
        if op == '+':
            sum += num
        elif op == '-':
            sum -= num
        elif op == '*':
            sum *= num
        else:
            if sum < 0:
                sum = -((-sum) // num)
            else:
                sum //= num
    if sum < min:
        min = sum
    if sum > max:
        max = sum

print(max)
print(min)
