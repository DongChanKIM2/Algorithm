def BruteForce(p, t):
    i = 0
    j = 0
    count = 0
    while i < n:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == m:
            count += 1
            j = 0
    if count > 0:
        return count
    else:
        return -1


for tc in range(1, 11):
    t = int(input())
    p = list(input())
    t = list(input())
    m = len(p)
    n = len(t)
    print('#{}'.format(tc), end=' ')
    print(BruteForce(p, t))

