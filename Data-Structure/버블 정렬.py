arr = [9, 8, 2, 7, 4]
# arr = [2, 3, 1, 2, 5, 9]
# arr = [4, 2, 6, 3, 7, 8, 1, 5]
# 버블 정렬 시간복잡도: N ** 2

arr = [9, 8, 2, 7, 4]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            print(arr)

# 병합 정렬 시간복잡도: 쪼갤 때 O(logN) + 합칠 때 O(N) = O(NlogN)
# 참조 사이트: https://www.youtube.com/watch?v=QAyl79dCO_k
# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#
#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])
#     merged_arr = []
#     print(low_arr, high_arr)
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     print(l, low_arr[l:], h, high_arr[h:], merged_arr)
#     return merged_arr
#
# print(merge_sort(arr))

# 퀵 정렬
# print(arr)