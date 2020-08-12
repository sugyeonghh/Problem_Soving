num = int(input())
num_list = input()

min = 1000000
max = -1000000

num_list = list(map(int,num_list.split(' ')))

for i in num_list:
    if i<min:
        min = i
    if i>max:
        max = i
        
print(str(min)+' '+str(max))