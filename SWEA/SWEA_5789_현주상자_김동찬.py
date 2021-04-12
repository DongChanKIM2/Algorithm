t = int(input())
for tc in range(t):
    n, q = list(map(int, input().split()))
    arr = [0] * n
    for i in range(q):
        l, r = list(map(int, input().split()))
        for idx in range(l-1, r):
            arr[idx] = i+1

    arr = map(str, arr)
    result = ' '.join(arr)
    print('#{} {}'.format((tc+1), result))
