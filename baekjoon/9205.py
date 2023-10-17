from sys import stdin
from collections import deque

def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x - festival[0]) + abs(y - festival[1]) <= distance:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                store_x, store_y = store[i]
                if abs(x - store_x) + abs(y - store_y) <= distance:
                    q.append([store_x, store_y])
                    visited[i] = 1
    print('sad')
    return

distance = 20 * 50
for t in range(int(input())):
    n = int(input())
    home = [int(x) for x in stdin.readline().split()]
    store = []
    for i in range(n):
        x, y = map(int, stdin.readline().split())
        store.append([x, y])
    festival = [int(x) for x in stdin.readline().split()]
    visited = [0 for i in range(n + 1)]
    bfs()
    