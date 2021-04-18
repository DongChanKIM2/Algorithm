def perm(level):
    if level >= N:
        print(arr)
        result_arr.append(arr.copy())
        return
    for i in range(N):
        if visited[i] == 1:
            continue
        else:
            visited[i] = 1
            arr[level] = A[i]
            perm(level+1)
            visited[i] = 0
            arr[level] = 0


A = [1, 2, 3] # 돌아가는 녀석 (출력될 놈은 아님)
N = len(A)
visited = [0] * 3
arr = [0] * 3
result_arr = []
perm(0)
print(result_arr)
