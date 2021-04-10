def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged_arr = []
    left = right = 0
    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] < right_arr[right]:
            merged_arr.append(left_arr[left])
            left += 1
        else:
            merged_arr.append(right_arr[right])
            right += 1
    merged_arr += left_arr[left:]
    merged_arr += right_arr[right:]
    print(merged_arr)
    return merged_arr


arr = list(map(int, input().split()))
merge_sort(arr)
# print(arr)
# print(merged_arr)
