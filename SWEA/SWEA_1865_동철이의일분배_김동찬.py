# import sys
# sys.stdin = open("input.txt")

def perm(level, result):
    global ans

    # 1번째 백트랙킹 조건
    if ans >= result:
        return

    if level >= N:
        if result > ans:
            ans = result
        return

    for i in range(N):
        if visited[i] == 0:
            arr[level] = A[i]
            visited[i] = 1
            # print(succees[level][arr[level]], factories[i][arr[i]])
            perm(level+1, result * float(succees[level][arr[level]])/100)
            arr[level] = 0
            visited[i] = 0


t = int(input())
for tc in range(t):
    N = int(input())

    visited = [0] * N
    arr = [0] * N

    A = [i for i in range(0, N)]

    succees = [list(map(int, input().split())) for _ in range(N)]
    ans = 0.0000000001
    perm(0, 1)
    print('#{} {:.6f}'.format(tc+1, ans * 100))
