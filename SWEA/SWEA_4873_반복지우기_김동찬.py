t = int(input())
for tc in range(t):
    arr = list(input())
    result = []

    for i in arr:
        result.append(i)
        if len(result) > 1:
            if result[-1] == result[-2]:
                result.pop()
                result.pop()

    print('#{} {}'.format(tc+1, len(result)))
