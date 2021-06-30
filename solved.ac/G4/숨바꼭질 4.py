# 구해야 되는 것
# 1. 몇초에 도달했는지와
# 2. 도달한 시간이 같다면 몇 번 가능한지
# 3. 이 문제는 진짜 조건이 세세하게 주어진 상태이다
# 3.1 N, K 이 같은 경우 K가 N보다 작을 경우 2가지 케이스 고려해줘야함

import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [1, -1]

ans = 0
def perm(idx):
    global ans
    if ans == 1:
        return
    # print(time_chk)
    # print(sel, idx)
    # print(sel_visited)
    if idx >= sel_len:
        ans = 1
        sel.reverse()
        for i in sel:
            print(i, end=' ')
        # print(sel)
        # for i in sel:
        #     print(* i)
    else:
        for i in range(3):
            if i == 2:
                if sel[idx-1] % 2 == 0:
                    nx = sel[idx-1] // 2
                else:
                    continue
            else:
                nx = sel[idx-1] + dx[i]
            # print(nx)
            if 0 <= nx <= 2*max(N, K) - 1:
                if time_chk[nx] == sel_visited[idx-1] - 1:
                    sel[idx] = nx
                    sel_visited[idx] = sel_visited[idx-1] - 1
                    perm(idx+1)
                    sel[idx] = 0
                    sel_visited[idx] = 0


def bfs(start, move):
    queue = deque()
    queue.append((start, move))
    while queue:
        curr, time = queue.popleft()
        for direction in range(3):
            if direction == 2:
                nx = curr * 2
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
    print(N)
else:
    if K > N:
        time_chk = [9999999] * (K*2)
        time_chk[N] = 0
        visit_chk = [0] * (K*2)
    else:
        time_chk = [9999999] * (N*2)
        time_chk[N] = 0
        visit_chk = [0] * (N*2)

    bfs(N, 0)
    print(time_chk[K])
    # print(visit_chk[K])
    # print(time_chk)
    # print(visit_chk)

    sel = [0] * (time_chk[K] + 1)
    sel_visited = [0] * (time_chk[K] + 1)
    sel_len = len(sel)
    sel[0], sel_visited[0] = K, time_chk[K]
    perm(1)




