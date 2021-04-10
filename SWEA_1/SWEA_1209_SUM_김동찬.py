def my_max(a, b):
    if a>b:
        return a
    else:
        return b


for tc in range(1, 11):
    n = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    total = 0

    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[i][j]
        total = my_max(temp, total)
        # if temp > total:
        #     total = temp

    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        total = my_max(temp, total)

        # if temp > total:
        #     total = temp

    temp = 0
    for i in range(100):
        temp += arr[i][i]
    total = my_max(temp, total)

    # if temp > total:
    #     total = temp

    temp = 0
    for i in range(100):
        temp += arr[i][99-i]
    total = my_max(temp, total)

    # if temp > total:
    #     total = temp
    print('#{} {}'.format(n, total))
