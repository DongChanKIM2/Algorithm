# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(arr, direction):
    global cnt
    queue = []
    queue.append((x, y, direction))
    while queue:
        print(queue)
        # 현재 위치 및 방향
        current_x, current_y, current_direction = queue.pop(0)
        # 방향이 바뀌는 걸 count 해주는 용도
        direction_change_cnt = 0
        # 4방향 탐색을 하자
        for i in range(4):
            direction_change_cnt += 1
            # 지금은 1이면 왼쪽회전이 아직 안됌 => 1을 만나면 이어서 회전할 수 있게 해줘야함
            # if current_direction == i:
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            n_direction = (current_direction + 3) % 4

            # 아직 청소가 안된 자리라면
            if arr[nx][ny] == 0:
                # 청소처리 +1, 방향 전환해주기
                cnt += 1
                arr[nx][ny] = 2
                queue.append((nx, ny, n_direction))
                break
            else:
                current_direction = n_direction

        n_direction = (current_direction + 2) % 4
        nx = current_x + dx[n_direction]
        ny = current_y + dy[n_direction]
        if arr[nx][ny] == 1:  # 벽이면 끝 (d)
            return
        else:
            queue.append((nx, ny, current_direction))

            # # 4방향 탐색 다 했는데 갈데가 없는 경우 => 후진을 해야 할때 앞에가 벽이어도 뒤에가 청소된 곳이면 후진을 할 수 있다 => 앞에 continue
            # if direction_change_cnt == 4:
            #     # 후진을 할 수 있는 경우
            #     if current_direction == 0 and arr[current_x+1][current_y] == 2:
            #         queue.append((current_x+1, current_y, current_direction))
            #     elif current_direction == 1 and arr[current_x][current_y-1] == 2:
            #         queue.append((current_x, current_y-1, current_direction))
            #     elif current_direction == 2 and arr[current_x-1][current_y] == 2:
            #         queue.append((current_x-1, current_y, current_direction))
            #     elif current_direction == 3 and arr[current_x][current_y+1] == 2:
            #         queue.append((current_x, current_y+1, current_direction))
            #
            #     # 벽이라 후진 못하고 끝나는 경우
            #     elif current_direction == 0 and arr[current_x][current_y-1] == 1:
            #         break
            #     elif current_direction == 1 and arr[current_x][current_y-1] == 1:
            #         break
            #     elif current_direction == 2 and arr[current_x-1][current_y] == 1:
            #         break
            #     elif current_direction == 3 and arr[current_x][current_y+1] == 1:
            #         break
            #     continue
            #
            # # 테두리에서 벗어나면 continue
            # if nx >= N or ny >= M or nx < 0 or ny < 0:
            #     continue
            # # 벽이어도 continue (2이면은 후진할수도 있기 때문에 제외)
            # if arr[nx][ny] == 1:
            #     continue




N, M = map(int, input().split())
x, y, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr[x][y] = 2
# 무조건 빈칸에서 로봇청소기가 시작하니까 cnt 1부터
cnt = 1
bfs(arr, direction)
print(cnt)
