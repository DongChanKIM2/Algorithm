# 구해야 되는 것
# 1. 몇초에 도달했는지와
# 2. 도달한 시간이 같다면 몇 번 가능한지
# 3. 이 문제는 진짜 조건이 세세하게 주어진 상태이다
# 3.1 N, K 이 같은 경우 K가 N보다 작을 경우 2가지 케이스 고려해줘야함
# 4. 숨바꼭질2와 달리 워프에선 시간이 안걸리므로 무한반복될 수 있음

from collections import deque
dx = [1, -1]


def bfs(start, move):
    queue = deque()
    queue.append((start, move))
    while queue:
        # print(queue, time_chk)
        curr, time = queue.popleft()
        for direction in range(3):
            if direction == 2:
                nx = curr * 2
                if 0 <= nx <= 2*max(N, K) - 1:
                    if time < time_chk[nx]:
                        time_chk[nx] = time
                        visit_chk[nx] = 1
                    # elif time == time_chk[nx]:
                    #     visit_chk[nx] += 1
                    else:
                        continue
                    queue.append((nx, time))
            else:
                nx = curr + dx[direction]
                if 0 <= nx <= 2*max(N, K) - 1:
                    if time + 1 < time_chk[nx]:
                        time_chk[nx] = time + 1
                        visit_chk[nx] = 1
                    elif time + 1 == time_chk[nx]:
                        visit_chk[nx] += 1
                    else:
                        continue
                    queue.append((nx, time+1))


N, K = map(int, input().split())
if N == K:
    print(0)
else:
    if K > N:
        time_chk = [9999999] * (K * 2)
        time_chk[N] = 0
        visit_chk = [0] * (K * 2)
    else:
        time_chk = [9999999] * (N * 2)
        time_chk[N] = 0
        visit_chk = [0] * (N * 2)

    bfs(N, 0)
    # print(time_chk)
    # print(visit_chk)
    print(time_chk[K])
    # print(visit_chk[K])
