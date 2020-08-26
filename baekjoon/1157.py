import sys

word = sys.stdin.readline().upper()
alp = []
for i in range(26):
    alp.append(0)

for i in word[:-1]:
    alp[(ord(i)-65)] += 1

m = max(alp)
m_idx = alp.index(m)
alp.pop(m_idx)
n = max(alp)
if m==n:
    print('?')
else:
    print(chr(m_idx+65))