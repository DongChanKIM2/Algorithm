# 조합 nCk 구현해보자
# level(몇번째 선택을 하는지, depth) / S는 시작점
def combi(level, s):
    if level >= k:
        # print(arr, sum(arr))
        if sum(arr.copy()) >= b:
            ans_lst.append(sum(arr.copy())-b)
        return
    for i in range(s, N-k+level+1):
        arr[level] = heights[i]
        combi(level+1, i+1)


t = int(input())
for tc in range(t):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    N = len(heights)
    ans_lst = []
    k = 2
    for k in range(1, len(heights)+1):
        arr = [0] * k
        # k = i
        combi(0, 0)

    print('#{} {}'.format(tc+1, min(ans_lst)))
    # print(len(ans_lst))