from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        visited = [0] * len(words)
        bfs(begin, target, words, visited)
        return visited[words.index(target)]

def bfs(begin, target, words, visited):
    queue = deque([begin])
    q_idx = 0
    while queue:
        q = queue.popleft()
        if q == target:
            return 0
        if q in words:
            q_idx = words.index(q)
        for i, w in enumerate(words):
            if compare(q, w) and not visited[i]:
                queue.append(w)
                visited[i] = visited[q_idx] + 1
    
        
def compare(a, b):
    answer = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            answer += 1
    return True if answer == len(a) - 1 else False
    
begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))