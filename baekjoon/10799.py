from sys import stdin

stack = list(stdin.readline().strip())
tmp = []
cnt = 0
for i in range(len(stack)):
	if stack[i] == '(':
		tmp.append(stack[i])
	elif stack[i] == ')':
		tmp.pop()
		cnt += 1 if stack[i-1] == ')' else len(tmp)
print(cnt)