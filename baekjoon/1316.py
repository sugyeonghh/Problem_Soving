import sys

alp = []
N = int(input())
result = N

for i in range(N):
    word = ''.join(sys.stdin.readline().split())
    for a in range(26):
        alp.append(-1)

    for idx,w in enumerate(word):
        new_idx = ord(w)-97
        if alp[new_idx] == -1 or idx-alp[new_idx] == 1:
            alp[new_idx] = idx
        else:
            result -= 1
            break
    alp.clear()

print(result)