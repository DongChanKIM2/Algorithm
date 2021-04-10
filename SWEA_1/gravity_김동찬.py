n = int(input())
for i in range(n):
    numbers = int(input())
    blocks_height = list(map(int, input().split()))
    ans = 0

    for i in range(0, numbers - 1):
        total = 0
        for j in range(i, len(blocks_height)):
            if blocks_height[i] > blocks_height[j]:
                total += 1

        if ans < total:
            ans = total

    print(ans)
