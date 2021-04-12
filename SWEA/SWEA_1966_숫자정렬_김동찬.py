def selectionsort(arr):
    for i in range(len(arr)-1):
        minimum = i
        # print(minimum)
        for j in range(i+1, len(arr)):
            if arr[minimum] > arr[j]:
                arr[minimum], arr[j] = arr[j], arr[minimum]
    return arr


t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print('#{}'.format(tc+1), end=' ')
    for i in selectionsort(arr):
        print(i, end = ' ')
    print()