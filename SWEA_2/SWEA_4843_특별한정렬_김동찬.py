def bubblesort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    bubblesort(arr)
    result = []
    for i in range(5):
        result.append(arr[-(i)-1])
        result.append(arr[i])

    print('#{}'.format(tc+1), end=' ')
    for i in result:
        print(i, end=' ')
    print()