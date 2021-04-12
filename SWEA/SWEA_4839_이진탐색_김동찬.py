def bs(start, end, x):
    count = 0
    while start <= end:
        count += 1
        center = (start + end) // 2
        if center == x:
            return count
        elif center > x:
            end = center
        elif center < x:
            start = center
    return False


t = int(input())
for tc in range(t):
    page, a, b = list(map(int, input().split()))
    if bs(1, page, a) < bs(1, page, b):
        print('#{} {}'.format(tc + 1, 'A'))
    elif bs(1, page, a) > bs(1, page, b):
        print('#{} {}'.format(tc + 1, 'B'))
    elif bs(1, page, a) == bs(1, page, b):
        print('#{} {}'.format(tc + 1, '0'))




