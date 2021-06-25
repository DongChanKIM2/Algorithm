# (0,0) (0,3) (0,6) (3,0) ... 순서대로 확장
# 첫 번째 반례: 모든 값을 0으로 줘보면?


def sudoku(temp_dic, x, y):
    for i in range(9):
        if arr[x][i] != 0 and temp_dic[arr[x][i]] == 0:
            temp_dic[arr[x][i]] = 1
        if arr[i][y] != 0 and temp_dic[arr[i][y]] == 0:
            temp_dic[arr[i][y]] = 1
    for i in range(1, 10):
        if temp_dic[i] == 0:
            arr[x][y] = i
            cnt_dict[i] = 1
            break


# arr = [list(map(int, input().split())) for _ in range(9)]
arr = [list(map(int, input())) for _ in range(9)]
for big_x in range(3):
    for big_y in range(3):
        cnt_dict = {i+1: 0 for i in range(9)}
        start_x = big_x * 3
        start_y = big_y * 3
        # 정사각형 cnt
        for small_x in range(3):
            for small_y in range(3):
                # print(big_x+small_x, big_y+small_y)
                if arr[start_x+small_x][start_y+small_y] != 0:
                    cnt_dict[arr[start_x+small_x][start_y+small_y]] = 1

        for small_x in range(3):
            for small_y in range(3):
                if arr[start_x + small_x][start_y + small_y] == 0:
                    temp_dic = {i+1: 0 for i in range(9)}
                    for key, value in cnt_dict.items():
                        if value == 1:
                            temp_dic[key] = 1
                    sudoku(temp_dic, start_x+small_x, start_y+small_y)
# print(arr)
# for i in arr:
#     print(*i)
for i in arr:
    for j in i:
        print(j, end=' ')
    print()


