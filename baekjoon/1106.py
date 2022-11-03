from sys import stdin

# people, num_of_city = map(int, stdin.readline().split())

# city = {}


# for _ in range(num_of_city):
# 	cost, n = map(int, stdin.readline().split())
# 	city[cost] = n

people = 10
num_of_city = 3
city = {3:1, 2:2, 1:3}
city = dict(sorted(city.items(), key=lambda x:x[1], reverse=True))
dp = [0 for _ in range(people+1)]

for i in range(people+1):
	dp[i] = dp[i]
		
	print(dp)
	

# city = {3:1}
# people = 10
# dp = [0 for _ in range(people+1)]

# for cost, n in city.items():
# 	for i in range(n, people + 1):
# 		dp[i] = dp[i-n] + cost
