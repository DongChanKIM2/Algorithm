def cheak(num):
    ans = 0
    while True:
        # 몫: a, 나머지: b
        a = num // 2
        b = num % 2
        # 정답에 나머지 추가
        ans += b
        num = a
        if num == 0:
            break
    return ans


N, K = map(int, input().split())

if K > N:
    print(0)
elif K == N:
    print(0)
else:
    i = N
    while True:
        if cheak(i) <= K:
            print(i-N)
            break
        # 상점에서 사야할 개수 추가
        else:
            i += 1
