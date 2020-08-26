import sys

num = sys.stdin.readline().split()
n1 = num[0]
n2 = num[1]
result = None

for i in range(3):
    if n1[3-i-1] > n2[3-i-1]:
        result = n1
        break
    elif n1[3-i-1] < n2[3-i-1]:
        result = n2
        break
    else:
        continue
    
print(int(result[::-1]))