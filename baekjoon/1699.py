n = int(input())
dp = [0 for i in range(n + 1)]
dp[1] = 1

num = 1
for i in range(1, n + 1):
	if i == pow(num + 1, 2):
		dp[i] = 1
		num += 1
	else:
		dp[i] = dp[i - pow(num, 2)] + 1

print(dp)
print(dp[-1])