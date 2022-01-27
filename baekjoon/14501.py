from sys import stdin

n = int(input())
t = [0]
p = [0]
dp = [0] * (n + 2)

for i in range(n):
	a, b = map(int, stdin.readline().split())
	t.append(a)
	p.append(b)

for i in range(1, n + 2):
	idx = i + t[i]
	if (idx <= n):
		dp[idx] = max(dp[idx], dp[i] + p[i])
	print(dp)
print(max(dp))