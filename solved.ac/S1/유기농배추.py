# 1. 배추흰지렁이는 본인위치, 좌우상하 5군데를 해충으로부터 보호
# 2. 0에서는 흰지렁이는 살 수 없으므로 완전탐색 DFS 문제
# 3. dfs 라 썻지만 bfs 로 풀려했는데 시간초과로 인해 BFS 로 변경하니 시간 초과 해결
# 4. 혹시나 하는 마음에 방문처리를 29번째줄, 즉 큐에 추가하기전에 해주니까 bfs 로도 풀렸다
# 5. 추가하기전에 해주면 중복된 정보를 처리하지 않기 때문에 더욱 절약할 수 있기 때문에
# 6. 코드 작성의 위치에 따라 메모리 및 시간 절약을 깨닫을 수 있는 문제였습니다
from collections import deque


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j):
    global cnt
    # queue = []
    # queue.append((i, j))
    queue = deque()
    queue.append((i, j))
    while queue:
        curr_x, curr_y = queue.popleft()
        # visited[curr_x][curr_y] = 1
        for direction in range(4):
            nx = curr_x + dx[direction]
            ny = curr_y + dy[direction]
            if nx >= M or nx < 0 or ny >= N or ny < 0:
                continue
            # 방문처리를 안해주면 계속 해맨다
            if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    # 방문처리해줄 0 배열 생성
    visited = [[0] * N for _ in range(M)]
    # 필요한 지렁이 수
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1
    # 완전탐색 실시(배추가 있고 탐색하지 않은 곳만)
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                cnt += 1
                dfs(i, j)
    print(cnt)
