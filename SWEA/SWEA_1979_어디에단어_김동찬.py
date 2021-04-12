t= int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    arr = []
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)

    result = []
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i][j] != 0:
                count += 1
                if j == n-1:
                    result.append(count)
            else:
                result.append(count)
                count = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j][i] != 0:
                count += 1
                if j == n-1:
                    result.append(count)
            else:
                result.append(count)
                count = 0

    total = 0
    for i in range(len(result)):
        if result[i] == m:
            total += 1
    print('#{} {}'.format(tc+1, total))
