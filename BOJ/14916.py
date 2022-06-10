n = int(input())
answer = 0

while n > 0:
    if n == 1 or n == 3:
        answer = -1
        break
    elif not n % 5:  # 5원으로 줄 수 있을 경우
        answer += n//5
        break
    else:
        answer += 1
        n -= 2

print(answer)