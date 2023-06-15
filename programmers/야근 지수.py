from heapq import heappush, heappop, heapify

def solution(n, works):
    heapify(max_heap := [-i for i in works])
    
    print(max_heap)
    
    while n:
        if max_heap[0] == 0: return 0
        max = heappop(max_heap)
        heappush(max_heap, max + 1)
        n -= 1
        
    return sum([i ** 2 for i in max_heap])
