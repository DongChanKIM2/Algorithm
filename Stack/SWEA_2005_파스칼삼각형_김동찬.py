t = int(input())
for tc in range(t):
    n = int(input())
    arr = [1]
    result = [1]
    print('#{}'.format(tc + 1))
    for _ in range(n):
        for i in arr:
            print(i, end=' ')
        for i in range(len(arr)-1):
            if len(arr) == 1:
                result.append(arr[i])
                result.append(1)
            else:
                result = result[1:len(result)]
                result.append(arr[i]+arr[i+1])
        result.append(1)
        arr = result
        print()
