t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    arr = []
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    total = 0
    for nx in range(n-m+1):
        for ny in range(n-m+1):
            count = 0
            for mx in range(m):
                for my in range(m):
                    count += arr[nx + mx][ny + my]
            if count > total:
                total = count
    print('#{} {}'.format(tc+1, total))