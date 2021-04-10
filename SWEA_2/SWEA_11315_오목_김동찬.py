t = int(input())
for tc in range(t):
    n = int(input())
    over = 0
    result = [list(input()) for _ in range(n)]

    # 8가지 방향 모두
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    # 8가지 방향을 하나씩 먼저 수행함
    for i in range(8):
        #  오목판 좌우
        for x in range(n):
            for y in range(n):
                count = 1
                # 오목판 좌표가 'o'이라면
                while result[x][y] == 'o':
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 방향이 한 가지이므로 테두리를 넘으면 break
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        break
                    # 그 다음 칸이 'o'이라면 좌표 변경 후 count
                    if result[nx][ny] == 'o':
                        x, y = nx, ny
                        count += 1
                    else:
                        break
                    # 5개 연속인것을 확인하면 break
                    if count == 5:
                        over = 1
                        break

    if over == 1:
        print('#{} {}'.format(tc+1, 'YES'))
    else:
        print('#{} {}'.format(tc+1, 'NO'))
