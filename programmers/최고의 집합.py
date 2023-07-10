def solution(n, s):
    if s / n < 1: return [-1]
    
    d, m = divmod(s, n)
    
    answer = [d for i in range(n)]
    
    while m > 0:
        answer[m] += 1
        m -= 1
    
    return answer
