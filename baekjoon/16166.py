n = int(input())
line = []
for i in range(n):
	line.append(list(map(int, input().split()))[1:])

for i in line:
	if (i.index(0) != -1):
		start = i.index(0)
		break





print(line)
print(start)
