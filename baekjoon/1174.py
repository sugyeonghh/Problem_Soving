from itertools import combinations

N = int(input())

nums = [0,1,2,3,4,5,6,7,8,9]
arr = []
for i in range(1,11):
	for j in combinations(nums, i):
		str_nums = list(map(str,reversed(list(j))))
		arr.append(int("".join(str_nums)))

arr.sort()
if N > len(arr):
	print(-1)
else:
	print(arr[N-1])
