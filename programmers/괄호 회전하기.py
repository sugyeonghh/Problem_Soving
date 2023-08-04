from collections import deque

# solution 1
# valid = {'{':'}', '(':')', '[':']'}

# def is_valid(q):
#     stack = []
#     while q:
#         data = q.popleft()
#         if data in '[({':
#             stack.append(data)
#         elif stack and valid[stack.pop()] == data:
#             continue
#         else:
#             return 0
#     return 1


# def solution(s):
#     size = len(s)
#     if size % 2:
#         return 0
#     s *= 2
#     answer = 0
#     for i in range(size):
#         answer += is_valid(deque(s[i:i+size]))
#     return answer

# solution 2
def is_valid(s):
    while True:
        if '[]' in s: s = s.replace('[]', '')
        elif '()' in s: s = s.replace('()', '')
        elif '{}' in s: s = s.replace('{}', '')
        else: return 0 if s else 1
    
def solution(s):
    q = deque(s)
    answer = 0
    for i in range(len(s)):
        answer += is_valid(''.join(q))
        q.rotate(-1)
    return answer


