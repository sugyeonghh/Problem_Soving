def solution(numbers):
    answer = []
    
    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)
        else:
            tmp = bin(i)[2:]
            idx = tmp.rfind('0')
            if (idx == -1):
                tmp = '10' + tmp[1:]
            else:
                tmp = tmp[0:idx] + '10' + tmp[idx+2:]
            answer.append(int(tmp, 2))
    return answer
