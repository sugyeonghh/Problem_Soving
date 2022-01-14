from sys import stdin

n = int(input())
arr = list(map(int, stdin.readline().split()))
dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
	if arr[i] > dp[i - 1] + arr[i]:
		dp[i] = arr[i]
	else:
		dp[i] = dp[i- 1] + arr[i]

print(max(dp))