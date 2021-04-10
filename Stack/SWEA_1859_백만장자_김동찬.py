t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0
    maximum = 0
    for i in range(n-1, -1, -1):
        temp = arr[i]
        if temp > maximum:
            maximum = temp
        else:
            total += (maximum - temp)
    print('#{} {}'.format(tc+1, total))
