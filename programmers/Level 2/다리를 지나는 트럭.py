from collections import deque


def solution(bridge_length, weight, truck_weights):
    time, arrived = 0, 0  # 경과 시간, 도착한 트럭
    bridge = [0] * bridge_length  # 다리
    queue = deque(truck_weights)  # 남은 트럭

    while arrived < len(truck_weights):  # 모두 도착할 때까지 반복
        time += 1  # 시간 경과
        top = bridge.pop(0)  # 다리 마지막 칸

        if top != 0:  # 다리 마지막 칸에 트럭이 있을 경우
            arrived += 1

        if queue:  # 출발하지 않은 트럭이 있을 경우
            if sum(bridge) + queue[0] <= weight:  # 트럭이 출발해도 될 경우
                bridge.append(queue.popleft())  # bridge에 추가
            else:
                bridge.append(0)

    return time