def dfs(start):
    global cnt
    # 맨 처음 start(1) 처리
    if visited[start] == 0:
        visited[start] = 1

    stack = []
    stack.append(start)
    
    while stack:
        # 현재 위치
        current = stack.pop()
        # 리스트에서 이웃한 위치 뽑아내기
        for neighbor in adjacent_lst[current]:
            # 방문하지 않은 곳이면 방문처리
            if visited[neighbor] == 0:
                cnt += 1
                stack.append(neighbor)
                visited[neighbor] = 1


T = int(input())
N = int(input())
# lst가 arr보다 시간에서 유리
adjacent_lst = [[] * (T+1) for _ in range(T+1)]
visited = [0] * (T+1)
cnt = 0
for _ in range(N):
    st, ed = map(int, input().split())
    adjacent_lst[st].append(ed)
    adjacent_lst[ed].append(st)
# 시작점이 무조건 1이니까
dfs(1)
print(cnt)
