# 2를 곱하거나 뒤에 1을 붙이거나 하면서 확장
# 거꾸로 생각하면 1은 어차피 2로 나눌 수 없기에 1이 나오면 무조건 1을 때야함
# 되게 빨리 풀렸는데 입력조건을 보고 bottom up으로는 시간초과 나는 걸 캐치했기 때문인 것 같다(DP훈련이 도움이 됨)


A, B = map(int, input().split())
ans = 1
while B > A:
    # print(A, B)
    if (B - 1) % 10 == 0:
        B = (B-1) // 10
    elif B % 2 == 0:
        B = B // 2
    else:
        break
    ans += 1
if A != B:
    print(-1)
else:
    print(ans)
