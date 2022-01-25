# FIFO(선입선출)
from collections import deque
# 데이터를 넣고 빼는 속도가 리스트에 비해 효율적

queue = deque() # 큐 구현을 위해 deque 라이브러리 사용

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
print(list(queue))
queue.reverse()
print(queue)
