from sys import stdin

MAX = 10 ** 6
dest = int(input())
num_of_broken = int(input())
broken = []

if num_of_broken:
	broken = stdin.readline().split()

if dest == 100:
	print(0)
else:
	moves = abs(dest - 100)
	for channel_int in range(MAX + 1):
		channel = str(channel_int)
		for idx, ch in enumerate(channel):
			if ch in broken:
				break
			elif idx == len(channel)-1:
				moves = min(moves, abs(dest-channel_int)+len(channel))
	print(moves)