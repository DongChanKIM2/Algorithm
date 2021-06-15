# 목표: 플러그를 빼는 최소의 횟수
# 전략
# 1. 뒤에 나오는 총 횟수보다 바로 뒤에 나오는 것들이 중요
# 2. 현재 꽂힌게 나중에 다 중복된다하더라도 그 사이에 다른게 있다면 교체를 해야함
# 3. 완전탐색과 유사하게 해야하므로 idx가 바뀔때마다 거리 초기화 및 측정을 해서 멀리 있는 애부터 콘센트 교체


N, K = map(int, input().split())
electrics = list(map(int, input().split()))
current_electric = []
distance = {}
ans = 0
for i in range(K):
    if electrics[i] in current_electric:
        continue
    if len(current_electric) < N:
        current_electric.append(electrics[i])
        continue
    # 플러그가 꽉 차 있고 중복되지 않은 애를 만나면 그 다음애부터 idx 갱신해주기
    # 우선 현재 쓰고 있는 전자기기들 딕셔너리 생성 후 중복 사용된다면 idx 변경
    for idx in range(1, 101):
        distance[idx] = 101
    for j in range(K-1, i, -1):
        distance[electrics[j]] = j
    far_idx, far_value = 0, 0
    for key, value in distance.items():
        if key in current_electric:
            if value > far_value:
                far_idx, far_value = key, value
    for k in range(len(current_electric)):
        if current_electric[k] == far_idx:
            current_electric[k] = 0
            current_electric[k] += electrics[i]
            ans += 1
            break

print(ans)