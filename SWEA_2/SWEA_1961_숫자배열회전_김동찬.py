def rotate(arr):
    reverse_arr = []
    for i in range(len(arr)-1, -1, -1):
        reverse_arr.append(arr[i])
    return reverse_arr


def transverse(reverse_arr):
    transverse_arr = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            transverse_arr[x][y] += reverse_arr[x][y]
    for i in range(len(transverse_arr)):
        for j in range(i, len(transverse_arr)):
            transverse_arr[i][j], transverse_arr[j][i] = transverse_arr[j][i], transverse_arr[i][j]
    return transverse_arr


t = int(input())
for tc in range(t):
    n = int(input())
    result = []
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(3):
        reverse_arr = rotate(arr)
        transverse_arr = transverse(reverse_arr)
        arr = transverse_arr
        result.append(transverse_arr)

    final_result = ''
    for k in range(n):
        for j in range(3):
            for i in range(n):
                final_result += str(result[j][k][i])

    print('#{}'.format(tc+1))
    for i in range(len(final_result)//n):
        print(final_result[i*n:i*n+n], end=' ')
        if i % 3 == 2:
            print()