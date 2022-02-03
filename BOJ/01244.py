def change(n):
    if switches[n]:
        switches[n] = 0
    else:
        switches[n] = 1
    return


n_switch = int(input())
switches = [-1] + list(map(int, input().split()))
n_student, students = int(input()), []
for _ in range(n_student):
    gender, num = map(int, input().split())

    if gender == 1:  # 남학생
        for i in range(num, n_switch + 1, num):
            change(i)

    else:  # 여학생
        change(num)
        left, right = num - 1, num + 1
        while left >= 1 and right <= n_switch:
            if switches[left] == switches[right]:
                change(left)
                change(right)
                left -= 1
                right += 1
            else:
                break

else:
    for i in range(1, n_switch, 20):
        print(*switches[i:i + 20])

