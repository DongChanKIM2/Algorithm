t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    x_init = 0
    y_init = 0
    x_temp = 0
    y_temp = 0
    status = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 2:
                x_init = x
                y_init = y
                break

    x_temp += x_init
    y_temp += y_init

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    x_prev = []
    y_prev = []
    while True:
        x_previous = x_temp
        y_previous = y_temp
        for direction in range(4):
            nx = x_temp + dx[direction]
            ny = y_temp + dy[direction]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 0:
                x_prev.append(x_temp)
                y_prev.append(y_temp)
                x_temp, y_temp = nx, ny
                arr[x_temp][y_temp] = 1
            if arr[nx][ny] == 3:
                x_temp, y_temp = nx, ny
                status = 1
        if status == 1:
            break
        elif (x_temp == x_previous) and (y_temp == y_previous):
            if x_prev:
                x_temp = x_prev.pop()
                y_temp = y_prev.pop()
            else:
                break
        # print(x_temp, y_temp)

    print('#{} {}'.format(tc+1, status))


