def dfs(v):
    print(v, end=' ')

    if visited[v] == 0:
        visited[v] = 1

    for neighbor in adjacent_lst[v]:
        if visited[neighbor] == 0:
            visited[neighbor] = 1
            dfs(neighbor)


def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    print(v, end=' ')
    while queue:
        current = queue.pop(0)
        for i in adjacent_lst[current]:
            if visited[i] == 0:
                print(i, end=' ')
                visited[i] = 1
                queue.append(i)


N, M, V = map(int, input().split())
adjacent_lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    start, end = map(int, input().split())
    adjacent_lst[start].append(end)
    adjacent_lst[end].append(start)
for k in range(N+1):
    adjacent_lst[k].sort()
dfs(V)
print()
visited = [0] * (N+1)
bfs(V)