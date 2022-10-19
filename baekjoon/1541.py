s = input().split('-')
nums = []
for i in s:
	tmp = i.split('+')
	tmp = list(map(int, tmp))
	nums.append(sum(tmp))
print(nums[0] - sum(nums[1:]))