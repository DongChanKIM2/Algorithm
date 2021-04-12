# T = int(input())
# for i in range(T):
#     n = int(input())
#     numbers = list(map(int, input().split(' ')))
#     for j in range(len(numbers)-1, 0, -1):
#         for k in range(0, j):
#             if numbers[k] > numbers[k+1]:
#                 numbers[k], numbers[k+1] = numbers[k+1], numbers[k]
#     print('# {} {}'.format(i+1, numbers[-1]-numbers[0]))

def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

T = int(input())
for i in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    Bubble_sort(numbers)

    print('# {} {}'.format(i, numbers[-1] - numbers[0]))