import sys

num = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
result = 0

word = ''.join(sys.stdin.readline().split())

for w in word:
    result += num[ord(w)-65]+1

print(result)