# 1. N * M 격자판 이고  N+1 번행에 성이 있음
# 2. 궁수는 3명 배치하고 동시에 공격
# 3. 거리가 D이하의 적 중에서
# 가장 가깝고(행), 거리가 같으면 왼쪽부터(열) 공격
# 4. 공격 이후 적들은 한칸씩 밑으로 이동하고 성에 도착하면 제외시킴
# 5. 적이 사라질 때 까지 위의 프로세스는 반복됨
from collections import deque
# 상, 좌, 우
dx = [-1, 0, 0]
dy = [0, -1, 1]


def bfs(archer_x, archer_y):
    visited = [[0] * M for _ in range(N + 1)]
    global targets
    queue = deque()
    queue.append((archer_x, archer_y))
    visited[archer_x][archer_y] = 1
    while queue:
        curr_x, curr_y = queue.popleft()
        # print(curr_x, curr_y)
        for direction in range(3):
            nx = curr_x + dx[direction]
            ny = curr_y + dy[direction]
            # print(nx, ny)
            if nx >= N+1 or ny >= M or nx < 0 or ny < 0:
                continue
            if visited[nx][ny] != 0:
                continue
            if arr[nx][ny] == 0:
                visited[nx][ny] = visited[curr_x][curr_y] + 1
                queue.append((nx, ny))
            if arr[nx][ny] == 1 and (abs(nx-archer_x) + abs(ny-archer_y)) <= D:
                print(11)
                targets.append((nx, ny))
                visited[nx][ny] = visited[curr_x][curr_y] + 1
                # break
    # print(targets)
    # print(arr)
    # print(visited)
    # targets = []
    # return targets

    # print(visited)

def kill():
    global targets
    targets = []
    # print(arr)
    for i in range(0, M):
        if arr[-1][i] == 2:
            bfs(N, i)
    # targets 된 애들 죽이고
    for j in targets:
        arr[j[0]][j[1]] = 0
    print(arr)
    # 한칸씩 전진해야함




def combi(level, start):
    if level >= K:
        for archer in combi_result_arr:
            arr[-1][archer] = 2
        # print(combi_result_arr)
        # print(arr)
        kill()
        for archer in combi_result_arr:
            arr[-1][archer] = 0

        return
    else:
        for i in range(start, N-K+level+1):
            combi_result_arr[level] = combi_arr[i]
            combi(level+1, i+1)


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
archers = [0] * M
arr.append(archers)

targets = []

combi_arr = [i for i in range(N)]
combi_length = len(combi_arr)
K = 3
combi_result_arr = [0] * K

# visited = [[0] * M for _ in range(N+1)]

combi(0, 0)
# print(targets)