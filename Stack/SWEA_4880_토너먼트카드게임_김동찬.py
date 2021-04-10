def rsp(a, b):
    if (a == 1 and b == 2) or (a == 2 and b == 1):
        return 2
    elif (a == 1 and b == 3) or (a == 3 and b == 1):
        return 1
    elif (a == 2 and b == 3) or (a == 3 and b == 2):
        return 3

def RecursivePower(c, n):
    if n == 1:
        return c
    if n % 2 == 0:
        y = RecursivePower(c, n/2)
        return y * y
    else:
        y = RecursivePower(c, (n-1)/2)
        return y * y * c


for tc in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))
    print(rsp(arr[0], arr[1]))
