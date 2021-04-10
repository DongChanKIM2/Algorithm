t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    count = 0
    for i in arr[0]:
        if i != 'W':
            count += 1
    for i in arr[-1]:
        if i != 'R':
            count += 1

    length = n - 2
    possibilities = []
    for white in range(length+1):
        for blue in range(length+1):
            for red in range(length+1):
                if blue >= 1 and (white+blue+red) == length:
                    possibilities.append((white, blue, red))

    new_arr = [[0]*m for _ in range(n-2)]
    for i in range(len(arr)-2):
        for j in range(m):
            new_arr[i][j] = arr[i+1][j]
    print(new_arr)
    total = 1000
    current = -1
    white, black, red = 0, 0, 0
    for i in possibilities:
        changing_count = 0
        white = i[0]
        black = i[1]
        red = i[2]
        # print(i)
        # print(white)
        # print(black)
        # print(red)
        for white_idx in range(white):
            if white_idx >= 0:
                current += 1
                if current >= 0:
                    if new_arr[current] != 'W':
                        changing_count += 1
                print(current)
                print()
        for black_idx in range(black):
            current += 1
            if current >= 0:
                if new_arr[current] != 'B':
                    changing_count += 1
            print(current)
            print()
        for red_idx in range(red):
            current += 1
            if current >= 0:
                if new_arr[current] != 'R':
                    changing_count += 1
            print(current)
        if total > changing_count:
            total = changing_count
            print(total)
    print('#{} {}'.format(tc+1, count+total))
