# 1. 올바른 괄호는 개행(여는 것)은 중복해도 상관없지면 폐행은 개행 역순대로 해야함
# 2. () => *2 / [] => *3
# 3. 스택문제는 풀때마다 느끼는 거지만 조건이 참 많다...
# 4. 시간단축을 위해 break문의 적절한 활용 필요


strings = input()
operators = ['(', ')', '[', ']']
stack = []
flag = 0
for string in strings:
    stack.append(string)
    temp = 0
    cnt = 1
    # print(stack, flag)
    if string not in operators:
        flag = 1
    if flag == 1:
        break
    if string == ')':
        for i in range(len(stack)-2, -1, -1):
            cnt += 1
            if type(stack[i]) == int:
                temp += stack[i]
            elif stack[i] == '(':
                for _ in range(cnt):
                    stack.pop()
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(temp * 2)
                break
            else:
                flag = 1
                break
    if string == ']':
        for i in range(len(stack)-2, -1, -1):
            cnt += 1
            if type(stack[i]) == int:
                temp += stack[i]
            elif stack[i] == '[':
                for _ in range(cnt):
                    stack.pop()
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(temp * 3)
                break
            else:
                flag = 1
                break
# print(stack)
if flag == 1:
    print(0)
else:
    for i in stack:
        if i in operators:
            print(0)
            break
    else:
        print(sum(stack))
