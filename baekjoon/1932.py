from sys import stdin

triangle = []
n = int(input())

for i in range(n):
    triangle.append(list(map(int, stdin.readline().split())))

for i in reversed(range(n - 1)):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
print(triangle[0][0])