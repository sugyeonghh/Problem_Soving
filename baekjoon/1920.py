from sys import stdin

n = int(stdin.readline())
nums = set(map(int, stdin.readline().split()))
m = int(stdin.readline())
find = list(map(int, stdin.readline().split()))

for i in find:
    print(1) if i in nums else print(0)
