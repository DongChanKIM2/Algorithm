def dfs(v):
    global cnt
    if visited[v] == 0:
        visited[v] = 1
        cnt += 1

    stack = [v]

    while stack:
        current = stack.pop()
        for neighbor in adjacent_lst[current]:
            if visited[neighbor] == 0:
                stack.append(neighbor)
                visited[neighbor] = 1


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    adjacent_lst = [[] for _ in range(N+1)]
    visited = [0] * (N + 1)
    cnt = 0
    for i in range(M):
        adjacent_lst[arr[i*2]].append(arr[i*2 + 1])
        adjacent_lst[arr[i*2 + 1]].append(arr[i*2])
    for j in range(1, N+1):
        dfs(j)
    print('#{} {}'.format(tc+1, cnt))
