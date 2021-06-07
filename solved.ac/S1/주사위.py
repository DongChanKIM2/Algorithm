N = int(input())
numbers = list(map(int, input().split()))
minimum_nums = []
# A F 비교해서 작은 값
if numbers[0] >= numbers[5]:
    minimum_nums.append(numbers[5])
else:
    minimum_nums.append(numbers[0])
# B E 비교해서 작은 값
if numbers[1] >= numbers[4]:
    minimum_nums.append(numbers[4])
else:
    minimum_nums.append(numbers[1])
# C D 비교해서 작은 값
if numbers[2] >= numbers[3]:
    minimum_nums.append(numbers[3])
else:
    minimum_nums.append(numbers[2])
numbers.sort()
minimum_nums.sort()
# print(numbers)
# print(minimum_nums)
ans = 0
if N == 1:
    for i in range(5):
        ans += numbers[i]
elif N == 2:
    ans = minimum_nums[0] * 8 + minimum_nums[1] * 8 + minimum_nums[2] * 4
    # ans = numbers[0] * 8 + numbers[1] * 8 + numbers[2] * 4
else:
    cnt = N ** 3 - ((N-2) ** 2 * (N-1))
    # print(cnt)
    # 전체 작은 거 / 맨 밑 모서리 / 중간 모서리들 / 맨 위 모서리 / 맨 위 모서리를 제외한 것들
    # ans = minimum_nums[0] * cnt + minimum_nums[1] * 4 + (N - 2) * 4 * minimum_nums[1] + (minimum_nums[1] * 4 + minimum_nums[2] * 4) + (N - 2) * 4 * minimum_nums[1]
    ans = minimum_nums[0] * cnt + minimum_nums[1] * 4 * N + minimum_nums[2] * 4 + (N - 2) * 4 * minimum_nums[1]
    # ans = minimum_nums[0]
    # ans = numbers[0] * cnt + numbers[1] * 4 + (N - 2) * 4 * numbers[1] + (numbers[1] * 4 + numbers[2] * 4) + (N - 2) * 4 * numbers[1]
print(ans)
