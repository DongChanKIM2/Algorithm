# 배열: 2**N 길이 -> 배열로 풀면 안되는 문제
# def search(arr, N, end_r, end_c):
#     global start
#     if arr[r][c] != 0:
#         return
#     if N == 1:
#         arr[end_r-1][end_c-1] = start
#         arr[end_r-1][end_c] = start+1
#         arr[end_r][end_c-1] = start+2
#         arr[end_r][end_c] = start+3
#         start += 4
#         return
#     else:
#         search(arr, N-1, end_r//2, end_c//2)
#         search(arr, N-1, end_r//2, end_c)
#         search(arr, N-1, end_r, end_c//2)
#         search(arr, N-1, end_r, end_c)
#
#
# N, r, c = map(int, input().split())
# arr = [[0] * (2 ** N) for _ in range(2 ** N)]
# start = 0
# end_r = end_c = (2 ** N) - 1
# search(arr, N, end_r, end_c)
# print(arr[r][c])



# 배열: 2**N 길이 -> 배열로 풀면 안되는 문제
def search(N, end_r, end_c, end):
    global start
    global ans
    print(N, end_r, end_c, end)
    if N == 1:
        if (r, c) == (end_r, end_c):
            ans = end
            return
        elif (r, c) == (end_r, end_c-1):
            ans = end - 1
            return
        elif (r, c) == (end_r-1, end_c):
            ans = end - 2
            return
        elif (r, c) == (end_r-1, end_c-1):
            ans = end - 3
            return
    else:
        if 0 <= r <= end_r // 2 and 0 <= c <= end_c // 2:
            search(N-1, end_r//2, end_c//2, int((end+1)*(1/4)-1))
        elif 0 <= r <= end_r // 2 and end_c//2 + 1 <= c <= end_c:
            search(N-1, end_r//2, end_c, int((end+1)*(2/4)-1))
        elif end_r//2 + 1 <= r <= end_r and 0 <= c <= end_c // 2:
            search(N-1, end_r, end_c//2, int((end+1)*(3/4)-1))
        elif end_r//2 + 1 <= r <= end_r and end_c//2 + 1 <= c <= end_c:
            search(N-1, end_r, end_c, end)


N, r, c = map(int, input().split())
start = 0
ans = 0
end = ((2 ** N) ** 2) - 1
end_r = end_c = (2 ** N) - 1
search(N, end_r, end_c, end)
print(ans)

