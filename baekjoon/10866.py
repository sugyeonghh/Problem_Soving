import sys

n = int(input())
deque = []
for i in range(n):
	command = list(sys.stdin.readline().split())
	comm = command[0]
	if comm == 'push_front':
		deque.insert(0, command[1])
	elif comm == 'push_back':
		deque.append(command[1])
	elif comm == 'pop_front':
		if deque:
			print(deque.pop(0))
		else:
			print(-1)
	elif comm == 'pop_back':
		if deque:
			print(deque.pop(-1))
		else:
			print(-1)
	elif comm == 'size':
		print(len(deque))
	elif comm == 'empty':
		if not deque:
			print(1)
		else:
			print(0)
	elif comm == 'front':
		if not deque:
			print(-1)
		else:
			print(deque[0])
	elif comm == 'back':
		if not deque:
			print(-1)
		else:
			print(deque[-1])
	else:
		break