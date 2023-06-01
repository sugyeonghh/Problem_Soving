def solution(n):
    prime = set()
    
    i = 2
    while i <= n:
        if n % i == 0:
            n /= i
            prime.add(i)
        else:
            i += 1

    return sorted(list(prime))