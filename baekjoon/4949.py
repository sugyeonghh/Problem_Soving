from sys import stdin

d = {'(':')', '[':']'}

while True:
	tmp = []
	res = 1
	line = stdin.readline()
	if line == '.\n':
		break
	for i in line:
		if i in '([':
			tmp.append(i)
		elif i in ')]':
			if tmp and d[tmp[-1]] == i:
				tmp.pop()
			else:
				res = 0
				break
	if tmp:
		res = 0
	print('yes' if res else 'no')