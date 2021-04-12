t = int(input())
for tc in range(t):
    arr = []
    count = 0
    n = int(input())
    for i in range(n):
        temp = list(map(int, input()))
        arr.append(temp)
    for i in range(len(arr)//2 + 1):
        for j in range((len(arr) // 2 - i), (len(arr) // 2 + i + 1)):
            count += arr[i][j]
    for i in range(len(arr)//2):
        for j in range((len(arr) // 2 - i), (len(arr) // 2 + i + 1)):
            count += arr[len(arr)-i-1][j]

    print('#{} {}'.format(tc+1, count))