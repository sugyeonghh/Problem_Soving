from sys import stdin

for t in range(int(stdin.readline())):
    case = []
    answer = 1
    for n in range(N := int(stdin.readline())):
        a, b = map(int, stdin.readline().split())
        case.append((a, b))
    case.sort()
    answer = 1
    min = case[0][1]
    for i in range(1, N):
        if min > case[i][1]:
            min = case[i][1]
            answer += 1
    print(answer)
