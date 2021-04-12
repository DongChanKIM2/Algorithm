t = int(input())
for tc in range(t):
    cards = list(input())
    result = []
    overlap = 0
    s, d, h, c = 13, 13, 13, 13
    s_num, d_num, h_num, c_num = 0, 0, 0, 0
    number = ''
    for i in range(0, len(cards), 3):
        temp = []
        for j in range(3):
            temp.append(cards[i+j])
        result.append(temp)

    for i in range(len(result)-1):
        for j in range(i+1, len(result)):
            if result[i] == result[j]:
                overlap = 1
                break

    for i in result:
        if i[0] == 'D':
            d -= 1
        if i[0] == 'S':
            s -= 1
        if i[0] == 'H':
            h -= 1
        if i[0] == 'C':
            c -= 1

    if overlap == 1:
        print('#{} {}'.format(tc + 1, 'ERROR'))
    else:
        print('#{} {} {} {} {}'.format(tc+1, s, d, h, c))

