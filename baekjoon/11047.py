
n, k = map(int, input().split())
idx = 0
coin = []
for i in range(n):
    coin.append(int(input()))

answer = 0
for i in reversed(coin):
    if i <= k:
        answer += k // i
        k %= i

print(answer)