# 서울의 지하철
# 그래프 탐색 / bfs / dijkstra

from sys import stdin
from collections import deque

n = int(stdin.readline().strip())

# make graph
graph1 = []
graph2 = []
line_num = []
visited = {}
for l in range(n):
	tmp = list(map(int, stdin.readline().split()))
	num = tmp[0]
	line = tmp[1:]
	for i in range(1, num):
		a1 = line[i - 1]
		a2 = line[i]
		if a1 in graph1:
			idx = graph1.index(a1)
			graph2[idx].append(a2)
			visited[a2] = 0
			line_num[idx].append(l + 1)
		else:
			graph1.append(a1)
			graph2.append([a2])
			visited[a1] = 0
			visited[a2] = 0
			line_num.append([l + 1])

arrival = int(stdin.readline().strip())
start = 0
result = 0

queue = deque()
visited[start] = 1
queue.append(start)
while queue:
	v = queue.popleft()
	if v in graph1:
		idx = graph1.index(v)
		for a in graph2[idx]:
			if a == arrival:
				break
			if a and not visited[a]:
				visited[a] = 1
				queue.append(a)

