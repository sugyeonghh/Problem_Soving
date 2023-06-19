from sys import stdin

k = int(stdin.readline())
rope = []
for i in range(k):
    rope.append(int(stdin.readline()))
rope.sort()

answer = max(rope)
for i in range(k):
    answer = max(answer, rope[i] * (k - i))
print(answer)