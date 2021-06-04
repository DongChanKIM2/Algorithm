def perm(level, suuum):
    global total
    global ans
    total = 0

    # print(level, sum, ans)
    # 1번째 백트랙킹 조건
    if suuum >= ans:
        return

    if level >= N:
        for i in range(len(arr)):
            total += int(factories[i][arr[i]])

            # 2번째 백트랙킹 조건
            # 시간초과가 나니까 줄여주자...
            if total > ans:
                return
        # print(total)

        # ans가 total보다 더 작으니까
        ans = total
        return

    for i in range(N):
        if visited[i] == 0:
            arr[level] = A[i]
            visited[i] = 1
            # print(i, level)
            print(factories[level][arr[level]], factories[i][arr[i]])
            perm(level+1, suuum + int(factories[level][arr[level]]))
            arr[level] = 0
            visited[i] = 0


t = int(input())
for tc in range(t):
    N = int(input())

    visited = [0] * N
    arr = [0] * N

    # [0, 1, 2]
    A = [i for i in range(0, N)]

    factories = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    ans = 150000
    perm(0, 0)
    print('#{} {}'.format(tc+1, ans))