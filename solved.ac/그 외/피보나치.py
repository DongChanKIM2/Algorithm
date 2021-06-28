N = int(input())
arr = [0] * (N+1)
if N >= 1:
    arr[1] = 1
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    for i in range(2, N+1):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr[-1])
    # print(arr[-1])