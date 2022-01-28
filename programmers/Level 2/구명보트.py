def solution(people, limit):
    answer = 0
    idx1, idx2 = 0, len(people) - 1
    people.sort()

    while idx1 <= idx2:
        if people[idx1] + people[idx2] <= limit:
            idx1 += 1
        idx2 -= 1
        answer += 1

    return answer
