import sys

temp = sys.stdin.readline().split()
A = int(temp[0])
B = int(temp[1])
C = int(temp[2])
result = 0

if C==B:
    result = -1
else:
    n = int(A/(C-B))
    result = n+1

print(result)