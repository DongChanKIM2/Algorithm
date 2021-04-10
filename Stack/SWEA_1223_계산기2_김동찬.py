def minus(stack, calculate):
    calculate.append(stack.pop())
    global top
    top -= 1


def plus(i):
    stack.append(i)
    global top
    top += 1


for tc in range(1, 11):
    n = int(input())
    arr = list(input())
    top = -1
    stack = []
    calculate = []
    for i in arr:
        if i != '+' and i != '*':
            calculate.append(i)
        if not stack and (i == '+' or i == '*'):
            stack.append(i)
            top += 1
        else:
            if i == '+':
                if stack[top] == '*':
                    minus(stack, calculate)
                    if top >= 0:
                        minus(stack, calculate)
                        plus(i)
                    else:
                        plus(i)
                else:
                    minus(stack, calculate)
                    plus(i)
            elif i == '*':
                if stack[top] == '*':
                    minus(stack, calculate)
                    plus(i)
                else:
                    plus(i)
    while stack:
        calculate.append(stack.pop())

    result = []
    for i in calculate:
        total = 0
        if i == '+':
            total = result[-2] + result[-1]
            result.pop()
            result.pop()
            result.append(total)
        elif i == '*':
            total = result[-2] * result[-1]
            result.pop()
            result.pop()
            result.append(total)
        else:
            result.append(int(i))

    # print(result)

    print('#{} {}'.format(tc, sum(result)))
