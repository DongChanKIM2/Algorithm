t = int(input())
for tc in range(t):
    arr = list(input().split())
    arr.reverse()
    stack = []
    status = 0

    if len(arr) >= 2:
        while len(stack) < 2:
            stack.append(arr.pop())
    else:
        status = 1
        break

    while len(arr) > 0:
        temp = 0
        if arr[-1] == '+':
            if len(stack) >= 2:
                temp = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(temp)
                arr.pop()
            else:
                status = 1
                break
        elif arr[-1] == '*':
            if len(stack) >= 2:
                temp = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(temp)
                arr.pop()
            else:
                status = 1
                break
        elif arr[-1] == '/':
            if len(stack) >= 2:
                temp = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
                arr.pop()
            else:
                status = 1
                break
        elif arr[-1] == '-':
            if len(stack) >= 2:
                temp = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
                arr.pop()
            else:
                status = 1
                break
        else:
            stack.append(arr.pop())

    if status == 1:
        print('#{} {}'.format(tc+1, 'error'))
    elif stack[1] == '.':
        print('#{} {}'.format(tc+1, int(stack[0])))
    else:
        print('#{} {}'.format(tc+1, 'error'))


