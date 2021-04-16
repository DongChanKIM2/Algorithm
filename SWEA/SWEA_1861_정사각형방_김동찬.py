import sys
sys.stdin = open("input.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or ny >= n or nx < 0 or ny < 0:
            continue
        if arr[nx][ny] == arr[x][y] + 1:
            visited[arr[x][y]] += 1


t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 원래 재귀로 풀려했으나 백트랙킹 조건이 너무 애매함... visited arr를 만들어서 풀자
    visited = [0] * (n ** 2 + 1)
    answers = [0] * (n ** 2 + 1)
    for x in range(n):
        for y in range(n):
            dfs(x, y)
    for i in range(len(visited)):
        cnt = 1
        if visited[i] == 1:
            for j in range(i, len(visited)):
                if visited[j] == 1:
                    cnt += 1
                elif visited[j] == 0:
                    answers[i] = cnt
                    break
    result = 0
    result_idx = 0
    for i in range(len(answers)):
        # print(answers[i])
        if answers[i] > result:
            # print(1)
            result = answers[i]
            result_idx = i
    print('#{} {} {}'.format(tc+1, result_idx, result))




