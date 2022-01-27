from sys import stdin
from collections import deque

l = list(stdin.readline().strip())
left = deque(l)
right = deque()
for _ in range(int(input())):
	commands = stdin.readline().split()
	comm = commands[0]
	if comm == 'L':
		if left:
			right.appendleft(left.pop())
	elif comm == 'D':
		if right:
			left.append(right.popleft())
	elif comm == 'B':
		if left:
			left.pop()
	elif comm == 'P':
		left.append(commands[1])
print(''.join(left + right))