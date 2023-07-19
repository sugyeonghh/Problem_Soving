from sys import stdin

N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

left = 1
right = max(trees)
while left <= right:
    h = (left + right) // 2
    total = sum([i-h for i in trees if i > h])
    if total < M:
        right = h - 1
    else:
        left = h + 1
print(right)
