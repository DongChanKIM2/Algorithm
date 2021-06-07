# 정답은 맞았는데 가로, 세로 9 by 9 이므로 순열로 풀면 최대 81! 이 되니까 당연히 시간초과...
# 다른 방법을 찾아보자

def perm(level):
    global ans
    if level >= N:
        temp_ans = 0
        for i in range(len(arr)-1, -1, -1):
            temp_ans += arr[i][0] * (10 ** (len(arr) - i - 1))
        if ans > temp_ans:
            return
        if temp_ans ** 0.5 == int(temp_ans ** 0.5):
            # 전체 길이 및 flag
            end = len(arr)
            flag = 0
            # 처음부터 탐색을 시작
            for start in range(len(arr)):
                # 0이 아닌걸 발견!하면
                if arr[start][0] != 0:
                    # 0 이 아닌게 끝자리면 볼것도 없음
                    if start == end - 1:
                        # print('temp:', arr, temp_ans)
                        break
                    # 0 이 아닌것보다 뒤에 더 숫자가 있다면
                    else:
                        col_diff = arr[start][1] - arr[start+1][1]
                        row_diff = arr[start][2] - arr[start+1][2]
                        for j in range(start, end-1):
                            if arr[j][1] - arr[j+1][1] != col_diff or arr[j][2] - arr[j+1][2] != row_diff:
                                flag = 1
                    break
        else:
            return

        if flag == 0:
            if temp_ans > ans:
                ans = temp_ans
            return
    else:
        for i in range(N):
            if visited[i] == 1:
                continue
            else:
                visited[i] = 1
                arr[level] = sorted_new_arr[i]
                perm(level + 1)
                arr[level] = (0, 0, 0)
                visited[i] = 0


N, M = map(int, input().split())
arr = []
for _ in range(N):
    numbers = int(input())
    temp = []
    for _ in range(M):
        divide = numbers % 10
        temp.append(divide)
        numbers //= 10
    temp.reverse()
    arr.append(temp)
# 행과 열의 인덱스가 포함된 배열을 만들어야 함
new_arr = []
for i in range(N):
    for j in range(M):
        new_arr.append((arr[i][j], i, j))
sorted_new_arr = sorted(new_arr, key=lambda x: x[0])
# print(sorted_new_arr)
# 내가 실제로 출력하고 싶은 길이와 배열 및 방문체크 배열
N = len(sorted_new_arr)
# 값 뿐만 아니라 행열 인덱스도 포함해서 만들어야함
arr = [[0] * 3] * N
visited = [0] * N
ans = 0
for i in range(N):
    perm(i)
if ans == 0:
    print(-1)
else:
    print(ans)

