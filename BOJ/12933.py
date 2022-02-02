sound, default = input(), 'quack'

if len(sound) % len(default):
    print(-1)
else:
    visited = [False] * len(sound)

    def sol():
        cnt, answer = 0, False
        for i, s in enumerate(sound):
            if not visited[i] and s == default[cnt]:
                cnt += 1
                visited[i] = True

            if s == 'k' and cnt == len(default):
                cnt = 0
                answer = True

        return answer

    total = 0
    while visited.count(False) > 0:
        if sol():
            total += 1
        else:
            print(-1)
            break
    else:
        print(total)

