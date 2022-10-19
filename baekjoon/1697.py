from collections import deque

MAX = 100000

def bfs(n, k):
	q = deque()
	q.append(n)
	while q:
		x = q.popleft()
		if x == k:
			print(depth[x])
			break
		for i in (x - 1, x + 1, 2 * x):
			if 0 <= i <= MAX and not depth[i]:
				depth[i] = depth[x] + 1
				q.append(i)

n, k = map(int, input().split())
depth = [0] * (MAX + 1)
bfs(n, k)