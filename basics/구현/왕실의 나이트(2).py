input_string = input()

lx = [-2, -2, -1, -1, 1, 1, 2, 2]
ly = [-1, 1, -2, 2, -2, 2, -1, 1]

x = int(input_string[1])
y = ord(input_string[0]) - ord('a') + 1

answer = 0
for i in range(len(lx)):
    nx, ny = x + lx[i], y + ly[i]
    if nx > 0 and nx <= 8 and ny > 0 and ny <= 8:
        answer += 1

print(answer)
