# https://www.youtube.com/watch?v=BLc3wzvycH8&t=15s 참조링크


def dfs(v, cnt):
    global ans
    # 우선 방문처리
    visited[v] = 1

    # ans보다 커지면 swap
    if cnt > ans:
        ans = cnt

    # 인접한 리스트 내부의 요소들 중
    for neighbor in adjacent_lst[v]:
        # 방문을 하지 않았더라면
        if visited[neighbor] == 0:
            # dfs 재귀
            dfs(neighbor, cnt+1)
            # 다시 방문 안했다고 백트랙킹
            visited[neighbor] = 0


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    # adj = [[0] * (N+1) for _ in range(N+1)]
    adjacent_lst = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end = map(int, input().split())
        adjacent_lst[start].append(end)
        adjacent_lst[end].append(start)
    ans = 0
    for j in range(1, N+1):
        # visited, cnt 초기화
        visited = [0] * (N+1)
        dfs(j, 1)

    print('#{} {}'.format(tc+1, ans))

