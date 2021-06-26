# 반례
# [0 0 0 0 0 0 0 0 0] * 9
ans = 0

def dfs(x, y, cnt_dict):
    print(x, y)
    global ans
    if ans == 1:
        return
    if cnt_dict.get(arr[x][y]) == 1:
        return
    if x == 8 and y == 8:
        print(111111111111111111111111)
        for i in arr:
            print(*i)
        ans = 1
        return
    flag = 0
    for i in range(1, 10):
        if cnt_dict[i] == 0:
            flag = 1
    if flag == 0:
        return
    else:
        for i in range(9):
            for j in range(9):
                if arr[i][j] != 0:
                    continue
                else:
                    cnt_dict = {i + 1: 0 for i in range(9)}
                    # 가로 세로 체크 및 9각형
                    for cnt in range(9):
                        if arr[i][cnt] != 0:
                            cnt_dict[arr[i][cnt]] = 1
                        if arr[cnt][j] != 0:
                            cnt_dict[arr[cnt][j]] = 1
                    first_x = i // 3
                    first_y = j // 3
                    first_x *= 3
                    first_y *= 3
                    for row in range(first_x, first_x+3):
                        for col in range(first_y, first_y+3):
                            if arr[row][col] != 0:
                                cnt_dict[arr[row][col]] = 1

                    for cnt in range(1, 10):
                        arr[i][j] = cnt
                        dfs(i, j, cnt_dict)
                        # return 된거면 다시 0으로 돌려야함
                        arr[i][j] = 0
                    # if j > 0:
                    #     dfs(i, j-1, cnt_dict)
                    # else:
                    #     dfs(i-1, 8, cnt_dict)


# arr = [list(map(int, input().split())) for _ in range(9)]
arr = [list(map(int, input())) for _ in range(9)]
cnt_dict = {i + 1: 0 for i in range(9)}
dfs(0, 0, cnt_dict)
print(arr)
