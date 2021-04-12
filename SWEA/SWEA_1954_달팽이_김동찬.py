t = int(input())
for tc in range(t):
    n = int(input())
    arr = []

    for i in range(n):
        temp_arr = [0] * n
        arr.append(temp_arr)
    arr[0][0] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0
    for j in range(3):
        for i in range(n-1):
            nx = x + dx[j]
            ny = y + dy[j]
            arr[nx][ny] = arr[x][y] + 1
            x, y = nx, ny

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(n**2-1):
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                x, y = nx, ny
                break

    new_arr = []
    print('#{}'.format(tc+1))
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()
