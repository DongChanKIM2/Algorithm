t = int(input())
for tc in range(t):
    arr = []
    for i in range(10):
        temp_arr = [0] * 10
        arr.append(temp_arr)
    n = int(input())
    for i in range(n):
        a, b, c, d, e = list(map(int, input().split()))
        for j in range(c-a+1):
            for k in range(d-b+1):
                arr[a+j][b+k] += e

    total = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                total += 1
    print('#{} {}'.format(tc+1, total))


