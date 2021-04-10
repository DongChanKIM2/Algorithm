# 시행착오 두 가지
# 1, distance_arr를 새로 만들어서 하니까 오히려 더 복잡함
# 2. for문 아닌 재귀문으로 하니 범위를 제한하지 못해서 전체 counting만 가능

def dfs(i, j):
    global count
    # 한번 밟았다
    count += 1
    # 우선 초기화
    arr[i][j] = 0
    # 4방향 탐색
    for direction in range(4):
        nx = i + dx[direction]
        ny = j + dy[direction]
        # 범위 제한
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        # 1이면 가자
        if arr[nx][ny] == 1:
            dfs(nx, ny)


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
counts = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        # 움직이면 초기화
        count = 0
        # 1일때 dfs탐색 시작
        if arr[i][j] == 1:
            dfs(i, j)
            counts.append(count)
print(len(counts))
counts.sort()
for count in counts:
    print(count)

