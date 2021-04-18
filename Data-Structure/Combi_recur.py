def combi(level, start):
    print(level, start)
    if level >= K:
        print(arr)
        return
    for i in range(start, N-K+level+1):
        arr[level] = A[i]
        combi(level+1, i+1)


A = [1, 2, 3, 4, 5]
N = len(A)
K = 3
arr = [0] * K
combi(0, 0)
