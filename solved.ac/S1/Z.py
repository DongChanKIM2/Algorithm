# N의 최대값이 15이므로 2**15*(2**15) 하면 터질듯 -> 필요한 부분만 잡아야함
# quarter 사분면 이동은 불필요하나 이동을 명시적으로 나타내고 싶어서 인수에 추가함

def z(N, r, c, quarter, start):
    # print(N, r, c, quarter, start)
    global ans
    if N == 1:
        if r == 0 and c == 0:
            start += 0
        elif r == 0 and c == 1:
            start += 1
        elif r == 1 and c == 0:
            start += 2
        elif r == 1 and c == 1:
            start += 3
        ans = start
    else:
        if r < (2 ** N) // 2 and c < (2 ** N) // 2:
            z(N-1, r, c, 1, start)
        elif r < (2 ** N) // 2 and (2 ** N)//2 <= c < (2 ** N):
            z(N-1, r, c - (2 ** N) // 2, 2, start + 2 ** ((N - 1) * 2) * 1)
        elif (2 ** N)//2 <= r < (2 ** N) and c < (2 ** N) // 2:
            z(N-1, r - (2 ** N) // 2, c, 3, start + 2 ** ((N - 1) * 2) * 2)
        elif (2 ** N)//2 <= r < (2 ** N) and (2 ** N)//2 <= c < (2 ** N):
            z(N-1, r - (2 ** N) // 2, c - (2 ** N) // 2, 4, start + 2 ** ((N - 1) * 2) * 3)


N, r, c = map(int, input().split())
start = 0
ans = 0
z(N, r, c, -1, start)
print(ans)
