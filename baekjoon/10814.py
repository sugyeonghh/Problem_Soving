from sys import stdin
import operator

lst = []
for _ in range(int(input())):
	age, name = stdin.readline().split()
	lst.append((int(age), name))

lst.sort(key = lambda x:x[0])

for i in lst:
	print(i[0], i[1])