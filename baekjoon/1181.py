from sys import stdin

word = []
for _ in range(int(input())):
	word.append(stdin.readline().strip())

s_word = list(dict.fromkeys(word))
s_word.sort()
s_word.sort(key=len)

print("\n".join(s_word))