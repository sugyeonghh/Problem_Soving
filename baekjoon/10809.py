alp = []
for i in range(26):
    alp.append(-1)

word = input()
for i,data in enumerate(word):
    if alp[(ord(data)-97)]== -1:
        alp[(ord(data)-97)] = i

alp = list(map(str,alp))
print(' '.join(alp))