def dfs(start):
    global cnt
    if visited[start] == 0:
        visited[start] = 1
    stack = []
    stack.append(start)
    while stack:
        current = stack.pop()
        for neighbor in adjacent_lst[current]:
            if visited[neighbor] == 0:
                cnt += 1
                stack.append(neighbor)
                # print(neighbor)
                visited[neighbor] = 1


T = int(input())
N = int(input())
adjacent_lst = [[] * (T+1) for _ in range(T+1)]
visited = [0] * (T+1)
cnt = 0
for _ in range(N):
    st, ed = map(int, input().split())
    adjacent_lst[st].append(ed)
    adjacent_lst[ed].append(st)
dfs(1)
print(cnt)
