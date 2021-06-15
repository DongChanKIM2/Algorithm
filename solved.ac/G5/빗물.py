# 맨 좌측, 맨 우측은 빗물이 새나가니까 고려할 필요 X
# 기준점을 옮겨다니면서 좌측의 최대값, 우측의 최대값을 구하고 둘 중 최소값을 구하면 되지 않을까
# 골드 문제 치곤 쉬운 문제(이전에 swea 에서 비슷한 빌딩 최소값을 풀어봐서 그런 거 같다)

H, W = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

if W <= 2:
    print(0)
else:
    for i in range(1, W-1):
        left_maximum = 0
        right_maximum = 0
        current_idx = i
        for left_idx in range(0, i):
            if arr[left_idx] > left_maximum:
                left_maximum = arr[left_idx]
        for right_idx in range(i+1, W):
            if arr[right_idx] > right_maximum:
                right_maximum = arr[right_idx]
        smaller = min(left_maximum, right_maximum)
        if arr[current_idx] < smaller:
            ans += (smaller - arr[current_idx])
        # print(current_idx, left_maximum, right_maximum, ans)

print(ans)