size = 100

# 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def BFS(r, c):
    global status
    # Q를 초기화
    Q = []
    Q.append((r, c))
    dist[r][c] = 1
    # Q에 요소가 존재할때까지만 돌 것(빈컨테이너가되면 멈춰버린다)
    while Q:
        curr_r, curr_c = Q.pop(0)
        # 4방향탐색
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            # 범위를 벗어나면 다른방향 탐색
            if nr < 0 or nr >= size or nc < 0 or nc >= size:
                continue
            # 갈 수 없는 자리거나 이미 방문한 경우
            if arr[nr][nc] == 1 or dist[nr][nc] != 0:
                continue
            if arr[nr][nc] == 3:
                status = 1
                break

            Q.append((nr, nc))
            dist[nr][nc] = dist[curr_r][curr_c] + 1


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(size)]  # 행의 길이만큼 만들어준다
    dist = [[0]*size for _ in range(size)]
    status = 0
    start_x, start_y = 0, 0
    # 입력이 끝났으면 처음 시작 위치 찾기
    for i in range(size):
        for j in range(size):
            if arr[i][j] == 2 and dist[i][j] == 0:
                start_x += i
                start_y += j
    BFS(start_x, start_y)
    print('#{} {}'.format(tc, status))

