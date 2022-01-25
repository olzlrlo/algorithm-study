import sys
input = sys.stdin.readline

str = input()
str = str.replace("()", " ")
answer, stick = 0, 0

for s in str[::-1]:
    if s == ')':
        answer += 1
        stick += 1
    elif s == '(':
        stick -= 1
    elif s == ' ':
        answer += stick

print(answer)
