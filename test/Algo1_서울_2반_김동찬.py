# 테스트 케이스 개수
t = int(input())
for tc in range(t):
    # 행, 열
    n, m = list(map(int,input().split()))
    # 나무
    arr = [list(map(int, input().split())) for _ in range(n)]
    maximum = 0
    maximum_idx = 0
    total = 0
    count = 0
    for i in range(m):
        # 나무의 열이 홀수 일때만
        if i % 2 == 0:
            for j in range(n):
                # 행->열이 아니라 열->행이므로 반대
                total += arr[j][i]
                count += 1
                # 나무의 비용이 최대일때 값, idx 변환
                if arr[j][i] >= maximum:
                    maximum = arr[j][i]
                    maximum_idx = i + 1
    print('#{} {} {} {} {}'.format(tc+1, total, count, maximum, maximum_idx))
