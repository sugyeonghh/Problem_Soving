# 시간 초과

MAX = 9876543210

def solve(N):
	cnt = 0
	for num in range(1, MAX + 1):
		s = str(num)
		is_decreasing = True
		for i in range(len(s)-1):
			if int(s[i]) <= int(s[i+1]):
				is_decreasing = False

				break
		if is_decreasing:
			cnt += 1
			if cnt == N:
				print(num)
				break

N = int(input())
if N == 0:
	print(0)
elif N >= 1023:
	print(-1)
else:
	solve(N)