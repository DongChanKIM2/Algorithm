t = int(input())
for tc in range(t):
    arr = []
    maximum_length = 0
    for i in range(5):
        temp = list(input())
        arr.append(temp)
        if len(temp) > maximum_length:
            maximum_length = len(temp)

    for i in range(len(arr)):
        if len(arr[i]) < maximum_length:
            for j in range(maximum_length-len(arr[i])):
                arr[i].append('')

    print('#{}'.format(tc+1), end=' ')
    for i in range(maximum_length):
        for j in range(len(arr)):
            print(arr[j][i], end='')
    print()