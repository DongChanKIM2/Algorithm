# 1. 청소 구역 (N by M)
# 2. 청소 프로세스
# 2.1 현재 위치 청소
# 2.2 내가 현재 바라보고 있는 방향의 왼쪽이 청소가 필요하면 왼쪽으로 회전하고 한칸 전진
# 2.3 2.1을 반복해 청소
# 2.4 왼쪽이 청소할 필요가 없다면 다시 회전 후 위의 작동 방법
# 3. 4방향 모두 청소가 되있다면
# 3.1 후진할 장소가 있다면 후진하고 반복
# 3.2 후진할 장소가 벽이라면 작동 stop
# 프로세스가 복잡해보이지만 결국 왼쪽으로 회전하고나서 앞에 직진 장소가 청소할 수 있는지 아닌지 판단하는 문제
# 하... 4방향 다 재귀로 돌려주다 깊이에서 터짐....미치겠네 검사를 해주고 재귀를 돌리는 방식으로 변경해야 함
# 한바퀴 다 청소할 곳이 없다면 기존의 처음 방향에서 후진 방향만 검사해주면 됨(나머지 방향은 고려x)


# 방향은 반시계(왼쪽) 방향으로 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def rotate(current_dir):
    if current_dir == 0:
        return 1
    elif current_dir == 1:
        return 2
    elif current_dir == 2:
        return 3
    elif current_dir == 3:
        return 0


def clean(arr, r, c, current_dir, direction_change, before):
    global ans
    # 청소가 안된 곳이면 일단 청소부터
    while True:
        if arr[r][c] == 0:
            ans += 1
            arr[r][c] = 2
        # 1. 우선 왼쪽 방향으로 회전을 해야 함 회전을 하고 바로 방향전환 +1 해줘야 함... 여기서 엄청 헤맴 ㅠ
        check = False
        for _ in range(4):
            rotated_dir = rotate(current_dir)
            direction_change += 1
            # 2. 회전된 방향 기준으로 앞칸의 청소할 곳인지 아닌지 판단하고 진행
            nx = r + dx[rotated_dir]
            ny = c + dy[rotated_dir]
            current_dir = rotated_dir
            if 0 <= nx < N and 0 <= ny < M:  # nx, ny가 그래프를 벗어나지 않는지 확인
                if arr[nx][ny] == 0:
                    before = []
                    r, c = nx, ny
                    check = True
                    clean(arr, r, c, current_dir, 0, before)
                    return
                  # 다른 작업을 수행하기 이전에 끝나는 조건을 먼저 추가해줘야함
        if check == 0:
            # 제자리로 돌아오고
            nx = r - dx[current_dir]
            ny = c - dy[current_dir]
            if 0 <= nx < N and 0 <= ny < M:  # nx, ny가 그래프를 벗어나지 않는지 확인
                if arr[nx][ny] == 2 and (nx, ny) not in before:  # 2라면 즉 이미 청소한 칸인경우 후진
                    r, c = nx, ny
                    before.append((r, c))
                    # clean(arr, r, c, current_dir, 0, before)
                elif arr[nx][ny] == 1:
                    break
            else:
                break


N, M = map(int, input().split())
# 청소기의 위치와 현재 바라보고 있는 방향
r, c, current_dir = map(int, input().split())
if current_dir == 1:
    current_dir = 3
elif current_dir == 3:
    current_dir = 1

# 방(빈칸은 0, 벽은 1) 청소된 칸과 벽은 구분해야하므로 청소하면 2로 바꾸자
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 4번 방향이 바뀌면 원상복귀가 된 거
direction_change = 0
# 이걸 안 해주면 벽으로 둘러싸인 장소에서 청소한 곳들을 무한히 헤맬 수 있음
before = []
clean(arr, r, c, current_dir, direction_change, before)
print(ans)
