from collections import deque

def bfs(start, words, target):
    visited = [False] * len(words)
    queue = deque([(start, 1)])
    
    while queue:
        v, depth = queue.popleft() # 노드 번호, 깊이
        visited[v] = True
        if words[v] == target: # target을 찾으면 return
            return depth
        
        for i in range(len(words)): # 모든 노드에 대해,
            if not visited[i]: # 아직 방문하지 않았다면,
                diff = 0 # 하나의 알파벳만 다른지 확인
                for j in range(len(target)):
                    if words[i][j] != words[v][j]:
                        diff += 1
                if diff == 1: # 하나의 알파벳만 다르면,
                    queue.append((i, depth + 1)) # 큐에 push

def solution(begin, target, words):
    if target not in words:
        return 0

    for i in range(len(words)):
        diff = 0
        for j in range(len(begin)):
            if begin[j] != words[i][j]:
                diff += 1
        if diff == 1:
            return bfs(i, words, target)
