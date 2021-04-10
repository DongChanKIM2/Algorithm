t = int(input())
for tc in range(t):
    str1 = list(input())
    str2 = list(input())
    # count = 0
    total = 0
    for i in str1:
        count = 0
        for j in range(len(str2)):
            if i == str2[j]:
                count += 1
        if count > total:
            total = count
    print('#{} {}'.format(tc+1, total))


