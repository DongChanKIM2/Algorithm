def BruteForce(p, t):
    i = 0
    j = 0
    while j < m and i < n:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == m:
        return i
    else:
        return -1


t = int(input())
for tc in range(t):
    p = input()
    t = input()
    n = len(t)
    m = len(p)
    if BruteForce(p, t) == -1:
        print('#{} {}'.format(tc+1, 0))
    else:
        print('#{} {}'.format(tc+1, 1))

# t = 'abcdefgh'
# if str2 in str1:
#     print(1)