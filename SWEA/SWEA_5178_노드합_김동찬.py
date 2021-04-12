t = int(input())
for tc in range(t):
    n, m, l = map(int, input().split())
    arr = [0] * (n+1)
    for i in range(m):
        idx, value = map(int, input().split())
        arr[idx] = value
    for j in range(n, 0, -1):
        if j == n / 2:
            arr[j] = arr[j*2]
        elif arr[j] == 0:
            arr[j] = arr[j*2] + arr[j*2 + 1]
    # print(arr)
    print('#{} {}'.format(tc+1, arr[l]))
