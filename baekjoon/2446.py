N = int(input())
star = '*'
for i in range(1,2*N-1,2):
    print((star*(2*N-i)).center(2*N,' '))

for i in range(1,2*N,2):
    print((star*i).center(2*N,' '))