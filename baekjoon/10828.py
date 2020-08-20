import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    command_list = list(map(str, sys.stdin.readline().split()))
    command = command_list[0]
    if command == 'push':
        stack.append(int(command_list[1]))

    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        if stack:
            print('0')
        else:
            print('1')

    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print('-1')
    
    else:
        break