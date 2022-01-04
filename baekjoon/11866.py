import sys

n, k = map(int, sys.stdin.readline().split())
queue = list(range(1, n + 1, 1))
res = []
i = 0
while queue:
	i += 1
	tmp = queue.pop(0)
	if i % k != 0:
		queue.append(tmp)
	else:
		res.append(tmp)
s = ", ".join(map(str, res))
print('<' + s + '>')