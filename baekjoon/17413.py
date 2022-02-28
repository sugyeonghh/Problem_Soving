from sys import stdin

line = list(stdin.readline().strip())
size = len(line)
i = 0
start = 0
while i < size:
	if line[i] == '<':
		i += 1
		while line[i] != '>':
			i += 1
		i += 1
	elif line[i].isalnum():
		start = i
		while i < size and line[i].isalnum():
			i += 1
		tmp = line[start:i]
		tmp.reverse()
		line[start:i] = tmp
	else:
		i += 1

print(''.join(line))