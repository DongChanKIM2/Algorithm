for tc in range(1, 11):
    n = int(input())
    arr = list(input())
    a_arr = []
    b_arr = []
    c_arr = []
    d_arr = []
    for i in arr:
        if i == '(' or i == ')':
            a_arr.append(i)
        elif i == '[' or i == ']':
            b_arr.append(i)
        elif i == '{' or i == '}':
            c_arr.append(i)
        elif i == '<' or i == '>':
            d_arr.append(i)

    result = []

    for i in range(len(a_arr)):
        result.append(a_arr[i])
        if len(result) > 1:
            if a_arr[i] == ')' and result[-2] == '(':
                result.pop()
                result.pop()

    for i in range(len(b_arr)):
        result.append(b_arr[i])
        if len(result) > 1:
            if b_arr[i] == ']' and result[-2] == '[':
                result.pop()
                result.pop()

    for i in range(len(c_arr)):
        result.append(c_arr[i])
        if len(result) > 1:
            if c_arr[i] == '}' and result[-2] == '{':
                result.pop()
                result.pop()
    for i in range(len(d_arr)):
        result.append(d_arr[i])
        if len(result) > 1:
            if d_arr[i] == '>' and result[-2] == '<':
                result.pop()
                result.pop()

    if not result:
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))
