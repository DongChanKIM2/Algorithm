# 최소합문제
# 투포인터 문제란 index를 시작점(start), 끝점(end) 각각 사용해서 푸는 문제로 시간 단축에 매우 효과적


N, S = map(int, input().split())
arr = list(map(int, input().split()))
# arr의 누적합 배열
sum_A = [0] * (N + 1)
for i in range(1, N + 1):
    sum_A[i] = sum_A[i-1] + arr[i-1]
# 수열의 최대길이 100,000 이므로 100,001 이면 최대값
ans = 100001
start = 0
end = 1

# S를 넘는 모든 경우의 수를 구하는 것
while start != N:
    # S를 넘으면 앞에서부터 줄이면서 ans 최소값 구하는 작업
    if sum_A[end] - sum_A[start] >= S:
        if ans > end - start:
            ans = end - start
        start += 1
    # S를 넘지 않았으면 끝점(end)를 먼저 끝까지 움직이고, 끝점이 끝에 도달하면 시작점(start) 이동
    else:
        if end != N:
            end += 1
        else:
            start += 1
if ans == 100001:
    print(0)
else:
    print(ans)
# 실패한 코드(시간초과)
# N, S = map(int, input().split())
# arr = list(map(int, input().split()))
# flag = 0
# ans = 0
# for i in range(1, N+1):
#     for j in range(N):
#         if sum(arr[j:j+i]) >= S:
#             flag = 1
#             ans = i
#             break
#     if flag == 1:
#         break
# print(ans)
