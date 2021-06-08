# 2 -> 1
# 3 -> 2
# 4 -> 3
# 5 ->
# N개가 있을 때 K개 이하로 만들 수 있으려면 상점에서 사야하는 최소값
# 물을 부으려면 양쪽 물의 양이 같아야함
# from collections import  deque


N, K = map(int, input().split())

ans = 0
bottles = [1] * N

# 물을 부을 필요가 없는 경우
if K > N:
    ans = K - N
elif K == N:
    ans = 0

# 물을 부어야 하는 경우
while len(bottles) > K:
    # bottles.sort()
    if bottles[0] == bottles[1]:
        bottles[1] *= 2
        bottles[1], bottles[-1] = bottles[-1], bottles[1]
        bottles.pop(0)
    else:
        ans += 1
        bottles.insert(0, 1)
        # bottles.sort()
        if bottles[0] == bottles[1]:
            bottles[1] *= 2
            bottles[1], bottles[-1] = bottles[-1], bottles[1]
            bottles.pop(0)

#     print(bottles)
# print(bottles)
print(ans)
