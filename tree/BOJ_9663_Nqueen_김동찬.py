def queen(row, arr):
    global cnt
    # row 높이가 맨밑에 도달했다면 +1 해주기
    if row == n:
        cnt += 1
        return
    # 한행씩 내려가면서 유효성검사(행, 열, 대각선) 진행하면서 재귀해보자
    else:
        # 행은 1씩 증가하니까 유효성검사가 필요없음
        row += 1
        for i in range(1, n+1):
            arr[row] = i
            # 넣기전에 열 유효성검사부터 해주자
            # 넣기전에 열, 대각선 유효성검사
            for j in range(1, row):
                # 열 검사부터
                if arr[j] == arr[row]:
                    break
                # 대각선 검사
                if (row-j) == abs(arr[row]-arr[j]):
                    break
            else:
                queen(row, arr)
    return cnt
            

n = int(input())
arr = [0] * (n+1)
cnt = 0
queen(0, arr)
print(cnt)
