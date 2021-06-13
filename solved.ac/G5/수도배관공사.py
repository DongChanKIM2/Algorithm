# D: 물까지의 거리 / P: 매입한 파이프 개수
D, P = map(int, input().split())
# L: 길이 / C: 용량
# 목표: 수도관을 만들어 길이가 D와 같게 할 때 가능한 최대 용량을 구하는 것
# 파이프를 합치는 건 다 가능하지만 용량은 최솟값으로

# 길이, 두께는 24비트 양의 정수로 최대값: 2 ** 24
# 2 ** 24 = 16777216 => 전체 배열로 만들어서 푸는건 메모리 초과
# 거리에 따라 값들을 담아주기
arr = [0] * (D + 1)
for i in range(P):
    L, C = map(int, input().split())
    # 초기값에서 빼는 경우는 항상 고려
    if C > arr[D - L]:
        arr[D-L] = C
    # print(arr)
    for j in range(D):
        if j >= L and arr[j] != 0:
            # print(arr)
            # arr[j-L] = C
            arr[j-L] = max(arr[j-L], min(C, arr[j]))
print(arr[0])

