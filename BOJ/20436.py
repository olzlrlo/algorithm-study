sL, sR = input().split()
string = input()

def find_point(s):
    keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

    for i in range(len(keyboard)):
        if s in keyboard[i]:
            x, y = i, keyboard[i].index(s)
            return x, y
time = 0
left, right = "qwertasdfgzxcv", "yuiophjklbnm"
sL, sR = find_point(sL), find_point(sR)

for s in string:
    x, y = find_point(s)
    if s in left:
        time += abs(sL[0] - x) + abs(sL[1] - y) + 1
        sL = (x, y)
        continue
    if s in right:
        time += abs(sR[0] - x) + abs(sR[1] - y) + 1
        sR = (x, y)

print(time)