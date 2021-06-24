# 1, 2, 3 을 활용해서 구할 수 있는 경우의 수 모두 구하기
# 1 -> 2 -> 3 순서대로 경우의 수를 더해가보면 될듯?

T = int(input())
for tc in range(T):
    N = int(input())
    # 1번째 풀이
    # 우선 1원짜리로는 무조건 다 한개씩 가능
    arr = [1] * (N+1)
    coin = [2, 3]
    for i in coin:
        for j in range(i, N+1):
            if j == i:
                arr[j] += 1
            elif j - i > 0:
                arr[j] = arr[j] + arr[j-i]
    print(arr[-1])


