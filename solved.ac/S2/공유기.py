# 처음에는 조합문제로 생각했으나 N(집의 개수)가 20만 이하인 걸 보고 조합으론 못 풀겠다 판단
# 가장 작은값, 중간값, 가장 큰 값을 고르는게 핵심인걸 파악
# 인 줄 알았으나 언제나 그렇듯이 잘못 파악한거였음
# 전체 값을 받고서 거리의 차이에 따라 이진탐색을 해야하는 문제(특정값 Target 을 찾는게 아니라 거리차이를 이진탐색하는 특이한 문제)


N, C = map(int, input().split())
arr = []
for i in range(N):
    # 집의 위치 전부 넣어주기
    house = int(input())
    arr.append(house)
# 정렬
arr.sort()
# 최소 거리차이, 최대 거리차이(최소 거리차이는 1로 일단 있다고 가정하는거야, 있든 없든 상관없어)
start = 1
end = arr[-1] - arr[0]
ans = 0
# 최소값이 최대값 이하라면 탐색 시작
while start <= end:
    # 와이파이 설치 최소 거리
    mid = (start + end) // 2
    # print(mid)
    # 공유기 설치 횟수(처음 집엔 무조건 설치한다 가정)
    cnt = 1
    # 시작이 되는 집의 위치를 정해줘야함
    curr_house = arr[0]
    # 중간값 후보와 중간값 후보의 이전 값의 차이가 중간값(와이파이 최소 설치 거리)보다 크면 설치
    # 명확히 말하면 이전 집은
    for i in range(1, len(arr)):
        if arr[i] - curr_house >= mid:
            cnt += 1
            curr_house = arr[i]

    # 공유기 설치 수가 주어진 공유기보다 많으면 설치 간격 거리르 넓혀야함
    # 이 거리는 정답보단 작지만 정답일 수 있으니 넣어줌
    if cnt >= C:
        start = mid + 1
        ans = mid
    elif cnt < C:
        end = mid - 1

print(ans)



