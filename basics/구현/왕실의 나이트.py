now = input()
row = int(now[1])
col = int(ord(now[0])) - int(ord('a')) + 1
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


result = 0
for move in moves:
    nrow, ncol = row + move[0], col + move[1]
    if nrow > 0 and nrow < 9 and ncol > 0 and ncol < 9:
        result += 1

print(result)
