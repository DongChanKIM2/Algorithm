def BruteForce(p, t):
    i = 0
    j = 0
    count = 0
    while i < m:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == n:
            count += 1
            j = 0
    if count > 0:
        return count
    else:
        return 0


tc = int(input())
for test in range(tc):
    t, p = input().split()
    m = len(t)
    n = len(p)
    count = BruteForce(p, t)
    print('#{} {}'.format(test+1, m - n*count + count))
