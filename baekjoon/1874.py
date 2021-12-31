n = int(input())
stack = []
tmp = []
res = []
num = 1
for i in range(n):
	stack.append(int(input()))
while num <= n:
	tmp.append(num)
	res.append('+')
	while tmp and tmp[-1] == stack[0]:
		stack.pop(0)
		tmp.pop()
		res.append('-')
	num += 1
if not tmp:
	for i in res:
		print(i)
else:
	print('NO')