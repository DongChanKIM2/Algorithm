for tc in range(1, 11):
    n = int(input())
    arr = list(input())
    top = -1
    stack = []
    calculate = []
    for i in arr:
        if i == '(':
            stack.append(i)
            top += 1
        elif i == '+' or i == '-':
            if stack[top] == '*' or stack[top] == '/' or stack[top] == '-' or stack[top] == '+':
                calculate.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
                top += 1
        elif i == '*' or i == '/':
            if stack[top] == '*' or stack[top] == '/':
                calculate.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
                top += 1
        elif i == ')':
            while stack[top] != '(':
                calculate.append(stack.pop())
                top -= 1
            stack.pop()
            top -= 1
        else:
            calculate.append(i)

    result = []
    for i in calculate:
        total = 0
        if i == '-':
            total += result[-2] - result[-1]
            for j in range(2):
                result.pop()
            result.append(total)
        elif i == '+':
            total += result[-2] + result[-1]
            for j in range(2):
                result.pop()
            result.append(total)
        elif i == '*':
            total += result[-2] * result[-1]
            for j in range(2):
                result.pop()
            result.append(total)
        elif i == '/':
            total += result[-2] / result[-1]
            for j in range(2):
                result.pop()
            result.append(total)
        else:
            result.append(int(i))
    print('#{} {}'.format(tc, int(result[0])))


# (6+5*(2-8)/2)