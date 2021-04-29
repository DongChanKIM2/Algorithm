# 1. N*N 크기, M 마리 물고리, 1 마리 상어
# 2. 아기상어 크기: 2
# 3. 아기상어는 자신보다 작은 물고기만 먹을 수 있음
# 4. BUT 사이즈가 같으면 지나가는건 OK
# 5.
# 5.1 더 이상 먹을 수 없을때(작은게없거나, 아예없거나) 엄마 호출
# 5.2 먹을 수 있는게 1마리라면 그 1마리 먹으러 출격
# 5.3 먹을 수 있는게 2마리이상이면 거리상 가까운거 > 위 > 왼쪽
# 6. 내 크기만큼의 횟수만큼 잡아먹으면 size 1 증가
# 목표: 엄마 부르기전까지 소요되는 시간
# from collections imp
# 상, 좌, 하, 우 로 하면 5.3 규칙 충족
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, size, eating_cnt, calling_mom):
    queue = []
    queue.append((x, y, size, eating_cnt, calling_mom))

    while queue:

        curr_x, curr_y, curr_size, curr_eat_cnt, curr_call = queue.pop(0)
        print(curr_x, curr_y, curr_size, curr_eat_cnt, curr_call)
        print(arr, curr_size)
        # 나보다 작은 애가 없다면 stop
        flag = 1
        for i in range(N):
            for j in range(N):
                # 0이 아니고 더 작은 물고기가 있으면
                if arr[i][j] != 0 and arr[i][j] < curr_size:
                    flag = 0
        if flag == 1:
            break

        # 작은애가 하나라도 있다면 탐색을 하자
        # 만약 내가 잡아먹으면 초기화를 시키는게 관건일듯
        for direction in range(4):
            nx = curr_x + dx[direction]
            ny = curr_y + dy[direction]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if arr[nx][ny] > curr_size:
                continue
            if visited[nx][ny] == 1:
                continue
            if arr[nx][ny] == 0:
                queue.append((nx, ny, curr_size, curr_eat_cnt, curr_call+1))
                visited[nx][ny] = 1
            elif arr[nx][ny] < curr_size:
                # 잡아먹으면 새롭게 시작하자
                queue = []
                arr[nx][ny] = 0
                if curr_eat_cnt + 1 == curr_size:
                    queue.append((nx, ny, curr_size+1, 0, curr_call+1))
                else:
                    queue.append((nx, ny, curr_size, curr_eat_cnt+1, curr_call+1))

                # 만약에 잡아먹었다면 방문처리 초기화해주자 새로 탐색할거니까
                for temp_x in range(N):
                    for temp_y in range(N):
                        visited[temp_x][temp_y] = 0

            elif arr[nx][ny] == curr_size and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, curr_size, curr_eat_cnt, curr_call+1))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for shark_x in range(N):
    for shark_y in range(N):
        if arr[shark_x][shark_y] == 9:
            arr[shark_x][shark_y] = 0
            visited[shark_x][shark_y] = 1
            bfs(shark_x, shark_y, 2, 0, 0)
