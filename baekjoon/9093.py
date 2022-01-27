from sys import stdin

for _ in range(int(input())):
	l = stdin.readline().split()
	for i in l:
		print(i[::-1], end = ' ')
	print()