from collections import deque

# 상향식
def solution1(x, y, n):
    graph = [0] * (y + 1)
     
    def bfs():
        queue = deque([x])
        while queue:
            pos = queue.popleft()
            if pos == y:
                return graph[pos]
            for num in [pos + n, pos * 2, pos * 3]:
                if num <= y and not graph[num]:
                    queue.append(num)
                    graph[num] = graph[pos] + 1
        return -1
    
    answer = bfs()
    return answer

# 하향식
def solution2(x, y, n):
    graph = [0] * (y + 1)
     
    def bfs():
        queue = deque([y])
        while queue:
            pos = int(queue.popleft())
            if pos == x:
                return graph[pos]
            for num in [pos - n, pos / 2, pos / 3]:
                if num >= x and (num * 10 % 10) == 0 and not graph[int(num)]:
                    queue.append(num)
                    graph[int(num)] = graph[pos] + 1
        return -1
    
    answer = bfs()
    return answer
