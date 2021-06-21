# 순열처럼 풀이
def perm(i):
    if i > 2:
        for idx in range(2, i):
            if i % idx == 0:
                # print('return')
                return
    if i >= 10 ** (N-1):
        print(i)
        return
    for idx in range(5):
        i = (i * 10) + second[idx]
        perm(i)
        i //= 10


N = int(input())
# 첫번째 들어가는 소수와 두번째부터 들어가는 소수는 다름
biggest = [2, 3, 5, 7]
second = [1, 3, 5, 7, 9]
for i in range(4):
    perm(biggest[i])
