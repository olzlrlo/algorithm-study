n = int(input())
status = []
for _ in range(n):
    status.append(list(map(int, input().split())))


def make_team(n, r):
    def generate(choices):
        def check_status(total, team):
            for i in team:
                for j in team:
                    if i != j:
                        total += status[i][j]
            return total

        if len(choices) == r:
            global min_val
            a = check_status(0, choices)
            b = check_status(0, [i for i in range(n) if i not in choices])
            min_val = min(abs(a - b), min_val)
            return

        start = choices[-1] + 1
        for nxt in range(start, n):
            choices.append(nxt)
            generate(choices)
            choices.pop()

    generate([0])


min_val = 10**9
make_team(n, n//2)
print(min_val)
