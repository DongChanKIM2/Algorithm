t = int(input())
for tc in range(t):
    arr = list(input())
    result = []
    ans = 1
    for i in arr:
        if i == '(' or i == '{':
            result.append(i)
        elif i == ')':
            if len(result) > 0:
                if result[-1] == '(':
                    result.pop()
                else:
                    result.append(i)
                    break
            else:
                result.append(i)
                break
        elif i == '}':
            if len(result) > 0:
                if result[-1] == '{':
                    result.pop()
                else:
                    result.append(i)
                    break
            else:
                result.append(i)
                break

    if not result:
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(tc+1, ans))
