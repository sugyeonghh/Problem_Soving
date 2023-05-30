from math import sqrt, gcd

g, l = map(int, input().split())
n = l // g

for i in reversed(range(1, int(sqrt(n)) + 1)):
    if n % i == 0:
        a = g * i
        b = g * (n // i)

        if gcd(a, b) == g:
            print(a, b)
            break
