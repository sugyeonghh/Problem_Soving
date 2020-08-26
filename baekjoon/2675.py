import sys

S = int(sys.stdin.readline())
P = []

for i in range(S):
    temp = sys.stdin.readline().split()
    N = int(temp.pop(0))
    word = temp.pop()
    new_word = ''
    for j in word:
        new_word += j*N
    P.append(new_word)

for i in P:
    print(i)