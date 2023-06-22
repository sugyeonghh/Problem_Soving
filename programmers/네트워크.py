from collections import deque

def bfs(v, computers):
    q = deque([v])
    while q:
        now = q.popleft()
        for i, value in enumerate(computers[now]):
            if value == 1:
                q.append(i)
                computers[now][i] = 0

def solution(n, computers):
    count = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                computers[i][j] = 0
                bfs(j, computers)
                count += 1
    return count