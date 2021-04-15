t = int(input())
for tc in range(t):
    temp = []
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                temp = arr[i]
    result = []

    for i in range(m-1, -1, -1):
        if temp[i] == 1:
            result = temp[i-55: i+1]
            break

    result = map(str, result)

    binary_numbers = "".join(result)

    decimals = []

    for i in range(8):
        temp = ''
        for j in range(7):
            temp += (binary_numbers[i * 7 + j])
        if '0001101' in temp:
            decimals.append(0)
        if '0011001' in temp:
            decimals.append(1)
        if '0010011' in temp:
            decimals.append(2)
        if '0111101' in temp:
            decimals.append(3)
        if '0100011' in temp:
            decimals.append(4)
        if '0110001' in temp:
            decimals.append(5)
        if '0101111' in temp:
            decimals.append(6)
        if '0111011' in temp:
            decimals.append(7)
        if '0110111' in temp:
            decimals.append(8)
        if '0001011' in temp:
            decimals.append(9)

    total = 0
    for i in range(len(decimals)):
        if i % 2 == 0:
            total += (decimals[i] * 3)
        else:
            total += decimals[i]

    if total % 10 == 0:
        print('#{} {}'.format(tc+1, sum(decimals)))
    else:
        print('#{} {}'.format(tc+1, 0))
