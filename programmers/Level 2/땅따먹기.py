def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
        # land[i][0] += max(land[i-1][:0] + land[i-1][1:])
        # land[i][1] += max(land[i-1][:1] + land[i-1][2:])
        # land[i][2] += max(land[i-1][:2] + land[i-1][3:])
        # land[i][3] += max(land[i-1][:3] + land[i-1][4:])

    return max(land[-1])