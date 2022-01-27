from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
queue = deque([i for i in range(1, n + 1)])
res = []
i = 0
while queue:
	i += 1
	tmp = queue.popleft()
	if i % k != 0:
		queue.append(tmp)
	else:
		res.append(tmp)
s = ", ".join(map(str, res))
print('<' + s + '>')