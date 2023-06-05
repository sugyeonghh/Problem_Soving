# from collections import deque
# queue를 이용한 방법 -> 시간초과

# n = int(input())
# MAX = n + 1
# answer = [MAX] * (max(n, 5) + 1)
# answer[3] = answer[5] = 1

# queue = deque([3, 5])

# while queue:
#     kg = queue.popleft()
#     answer[kg] = min(answer[kg], answer[kg-3]+1, answer[kg-5]+1)
#     if kg+3 <= n:
#         queue.append(kg+3)
#     if kg+5 <= n:
#         queue.append(kg+5)

# print(answer[n] if answer[n] != MAX else -1)

n = int(input())
dp = [-1] * (max(n, 5) + 1)
dp[3] = dp[5] = 1

for i in range(6, n + 1):
    if dp[i - 3] > 0 and dp[i - 5] > 0:
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    elif dp[i - 3] < 0 and dp[i - 5] < 0:
        dp[i] = -1
    else:
        dp[i] = max(dp[i - 3], dp[i - 5]) + 1
        
print(dp[n])
