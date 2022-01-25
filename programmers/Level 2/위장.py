def solution(clothes):
    answer = 1
    closet = dict()

    for name, kind in clothes:
        if kind not in closet:
            closet[kind] = []
        closet[kind].append(name)

    for value in closet.values():
        answer *= len(value) + 1

    return answer - 1
