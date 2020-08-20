num_list = []
for i in range(10):
    flag = 1
    num = int(input())%42
    if not num_list:
        num_list.append(num)
    else:
        for i in num_list:
            if num == i:
                flag = 0
                break
        if flag:
            num_list.append(num)
            
print(len(num_list))