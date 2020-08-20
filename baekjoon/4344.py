C = int(input())
per = []
for i in range(C):
    case = list(map(int,input().split()))
    N = case.pop(0)
    avg = sum(case, 0.0)/N

    count = 0
    for i in case:
        if i>avg:
            count += 1
    per.append('%.3f'%(count/N*100))

for i in per:
    print(str(i)+'%')