from string import ascii_lowercase

def solution(s, skip, index):
    alpha = list(ascii_lowercase)
    for i in skip:
        if i in alpha:
            alpha.remove(i)
            
    answer = ''
    for i in list(s):
        answer += alpha[(alpha.index(i) + index) % len(alpha)]
    
    return answer    
