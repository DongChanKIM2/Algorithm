t = int(input())
for tc in range(t):
    arr = [list(map(int, input().split())) for _ in range(9)]
    over = 1

    for i in range(9):
        count_arr = [0] * 10
        for j in range(9):
            count_arr[arr[i][j]] += 1
        for count_idx in range(1, 10):
            if count_arr[count_idx] != 1:
                over = 0

    for i in range(9):
        count_arr = [0] * 10
        for j in range(9):
            count_arr[arr[j][i]] += 1
        for count_idx in range(1, 10):
            if count_arr[count_idx] != 1:
                over = 0

    for i in range(3):
        for j in range(3):
            count_arr = [0] * 10
            for small_i in range(3):
                for small_k in range(3):
                    count_arr[arr[i * 3 + small_i][j * 3 + small_k]] += 1
            for count_idx in range(1, 10):
                if count_arr[count_idx] != 1:
                    over = 0

    print('#{} {}'.format(tc + 1, over))