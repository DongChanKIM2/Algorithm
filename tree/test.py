def fibo(n):
    if n >= 2:
        arr[-1] = arr[-2] = 1
    for i in range(n, 0, -1):
        if arr[i] == 0:
            arr[i] = arr[i+1] + arr[i+2]
    return arr

n = int(input())
arr = [0] * (n+1)

print(fibo(n))