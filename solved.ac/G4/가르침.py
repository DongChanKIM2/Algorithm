# 단어의 개수는 N개이고 가르칠 수 있는 글자는 k개
# 시작: anta 끝: tica
# 1 <= N <= 50 / 0 <= k <= 26
# 목표: 읽을 수 있는 단어(N)의 최대값
# 1. 조합으로 가능할수도?


def combination(idx, sidx):
    global ans
    # print(K, sel)
    temp = 0
    if sidx == K:
        for i in range(N):
            for j in words[i]:
                if j not in sel:
                    break
            else:
                temp += 1
        if temp > ans:
            ans = temp
        return
    if idx == alpha_len:
        return
    sel[sidx] = alpha[idx]
    combination(idx+1, sidx+1)
    combination(idx+1, sidx)


N, K = map(int, input().split())
alpha = ['b', 'd', 'e', 'f', 'g',
         'h', 'j', 'k', 'l', 'm',
         'o', 'p', 'q', 'r', 's', 'u',
         'v', 'w', 'x', 'y', 'z']
alpha_len = len(alpha)

ans = 0
words = []
for i in range(N):
    word = list(input())
    temp = []
    for j in word:
        if j != 'a' and j != 'c' and j != 'i' and j != 't' and j != 'n' and j not in temp:
            temp.append(j)
    words.append(temp)
if K < 5:
    print(0)
else:
    K -= 5
    sel = [0] * K
    # print(words)
    combination(0, 0)
    print(ans)
