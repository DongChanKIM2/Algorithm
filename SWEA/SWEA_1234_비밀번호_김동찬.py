for tc in range(1, 11):
    n, m = input().split()
    result = []
    n = int(n)
    m = str(m)
    for i in range(n):
        result.append(m[i])
        if len(result) > 1:
            if result[-2] == result[-1]:
                result.pop()
                result.pop()

    print('#{}'.format(tc), end=' ')
    for i in result:
        print(i, end='')
    print()