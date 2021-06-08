# 높다고 다 보이는게 아니라 A기준 빌딩과 B 다른 빌딩의 지붕의 선분이 다른 건물에 접하거나 지나가면 안됌
# 1. 꼭대기간의 직선의 방정식을 구하고
# 2. 지나거나 접히는게 없으면 보이는 것
# 3. N=50 이므로 50*50=2500으로 시간문제는 없을 듯
# 4. 골드문제들 중 처음으로 풀자마자 맞춤!!! 생각보다 문제의 핵심만 짚으면 쉬운 문제 같음


N = int(input())
buildings = list(map(int, input().split()))
ans = 0
for i in range(len(buildings)):
    cnt = 0
    cnt_l = 0
    cnt_r = 0
    left = []
    right = []
    # 최대값들보다 기울기가 더 크면 접하거나 겹치지 않음
    left_maximum = -99999999999999999
    right_maximum = -99999999999999999
    for j in range(len(buildings)):
        if i != j:
            # 기준점보다 보는 빌딩이 오른쪽일때
            if j > i:
                # print((buildings[j]-buildings[i])/(j-i), end=' ')
                right.append((buildings[j]-buildings[i])/(j-i))
            # 왼쪽일때
            else:
                # print((buildings[i]-buildings[j])/(j-i), end=' ')
                left.append((buildings[i]-buildings[j])/(j-i))
    left.reverse()
    for l_idx in range(len(left)):
        if left[l_idx] > left_maximum:
            left_maximum = left[l_idx]
            cnt_l += 1
    for r_idx in range(len(right)):
        if right[r_idx] > right_maximum:
            right_maximum = right[r_idx]
            cnt_r += 1

    cnt = cnt_l + cnt_r

    if cnt > ans:
        ans = cnt

print(ans)