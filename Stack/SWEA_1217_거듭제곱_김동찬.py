def RecursivePower(c, n):
    if n == 1:
        return c
    if n % 2 == 0:
        y = RecursivePower(c, n / 2)
        return y * y
    else:
        y = RecursivePower(c, (n - 1) / 2)
        return y * y * c


for tc in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())
    print('#{}'.format(tc), end=' ')
    print(RecursivePower(n, m))