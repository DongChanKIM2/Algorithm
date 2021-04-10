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
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            # 갈 수 없는 자리거나 이미 방문한 경우
            if arr[nr][nc] == 1 or dist[nr][nc] != 0:
                continue
            if arr[nr][nc] == 3:
                status = 1
                result.append(dist[curr_r][curr_c]-1)
                break
                # return 1

            Q.append((nr, nc))
            dist[nr][nc] = dist[curr_r][curr_c] + 1
    # return 0

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]  # 행의 길이만큼 만들어준다
    dist = [[0]*n for _ in range(n)]
    status = 0 # 아니면 queue 끝에 return 0으로 해결가능
    result = []
    start_x, start_y = 0, 0
    # 입력이 끝났으면 처음 시작 위치 찾기 -> 함수로 만들어서 적용해보자
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2 and dist[i][j] == 0:
                start_x += i
                start_y += j
    BFS(start_x, start_y)
    if result:
        print('#{} {}'.format(tc+1, min(result)))
    else:
        print('#{} {}'.format(tc+1, 0))

    # print(dist)
    # print(result)
