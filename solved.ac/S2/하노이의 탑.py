# A B C 막대가 있다면
# A B 로 우선 VIA로 N-1개 옮기고
# A C 옮기는거 print 출력해주고
# B C 옮기기

def hanoi(N, start, end, via):
    if N == 1:
        print(start, end)
        return
    else:
        hanoi(N-1, start, via, end)
        print(start, end)
        hanoi(N-1, via, end, start)


N = int(input())
print(2 ** N - 1)
if N <= 20:
    hanoi(N, 1, 3, 2)
