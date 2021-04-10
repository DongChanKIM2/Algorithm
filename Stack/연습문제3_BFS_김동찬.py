def bfs(graph, v):
    visited = [0] * n
    visited[v] = 1
    queue = []
    queue.append(v)
    while queue:
        temp = queue.pop(0)
        print(temp)
        for i in range(n):
            if graph[temp][i] and visited[i] == 0:
                queue.append(i)
                visited[i] = 1


n, m = map(int, input().split())
lines = list(map(int, input().split()))
even_arr = []
odd_arr = []
for i in range(len(lines)):
    if i % 2:
        odd_arr.append(lines[i])
    else:
        even_arr.append(lines[i])
graph = [[0]*n for _ in range(n)]

for i in range(m):
    graph[even_arr[i]-1][odd_arr[i]-1] = 1
    graph[odd_arr[i]-1][even_arr[i]-1] = 1

bfs(graph, 0)
