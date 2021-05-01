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
# 방향설정을 상하좌우로만 하고 queue로 풀면 문제 발생(tc4와 같이) -> 일단 담아주고 거리에 따라 정렬을 해주는 필요성 제기
# 이 코드의 가장 큰 문제점: 탐색을 하면서 잡아먹고 visited를 초기화해주니까 시간적으로는 유리할 수 있어도 방향 설정 정밀 탈락
# 어떻게 고쳐야 되니? bfs를 하면서 잡아먹는게 아니고 bfs하고 잡아먹고 bfs하고 잡아먹고를 반복........ 

# 상 하 좌 우 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# x좌표, y좌표, 상어 크기, 몇 번 먹었는지, 엄마 부르기 시간
def bfs(x, y, size, eating_cnt, calling_mom):
    global flag
    queue = []
    queue.append((x, y, size, eating_cnt, calling_mom))
    while queue:
        curr_x, curr_y, curr_size, curr_eat_cnt, curr_call = queue.pop(0)

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
            # 작은 물고리를 거리별로 찾아서 제일 가까운 애를 먼저 찾으니까 잡아 먹으면 -> visited 초기화
            if visited[nx][ny] == 1:
                continue

            if arr[nx][ny] == 0:
                queue.append((nx, ny, curr_size, curr_eat_cnt, curr_call+1))
                visited[nx][ny] = 1

            # 잡아먹을 수 있는애들
            elif arr[nx][ny] < curr_size:
                visited[nx][ny] = 1
                
                # 잡아먹을 수 있으면 queue(이동경로)외에 feed(먹이 대상에 포함해주자)
                queue.append((nx, ny, curr_size, curr_eat_cnt, curr_call+1))
                feed.append((nx, ny, curr_size, curr_eat_cnt, curr_call+1))

            # 사이즈가 같아서 갈 수 있는 친구들
            elif arr[nx][ny] == curr_size:
                visited[nx][ny] = 1
                queue.append((nx, ny, curr_size, curr_eat_cnt, curr_call+1))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
feed = []
for shark_x in range(N):
    for shark_y in range(N):
        if arr[shark_x][shark_y] == 9:
            arr[shark_x][shark_y] = 0
            bfs(shark_x, shark_y, 2, 0, 0)
ans = 0
flag = 0

while True:
    # 거리, 높낮이, 왼쪽오른쪽 순으로 정렬
    feed.sort(key=lambda x: (x[4], x[0], x[1]))

    # 방문처리 매번 초기화
    visited = [[0] * N for _ in range(N)]
    # 먹이 대상이 없다면 멈춰!!
    if not feed:
        break
    else:
        a, b, c, d, e = feed.pop(0)
        feed = []
        # 먹을 친구니까 빈자리만 남기자
        arr[a][b] = 0
        ans = e
        # 한 번더 먹어서 사이즈 커지는지 아닌지 분류해서 다시 bfs 수행
        if c == d+1:
            bfs(a, b, c+1, 0, e)
        else:
            bfs(a, b, c, d+1, e)

print(ans)
