def solution(sequence, k):
    l = r = 0
    answer = [0, len(sequence)]
    
    while l >= 0 and r <= len(sequence)+1:
        if sum(sequence[l:r]) < k:
            r += 1
        elif sum(sequence[l:r]) > k:
            l += 1
        else:
            if r-l < answer[1]-answer[0]-1:
                answer = [l, r-1]
            l += 1
    return answer