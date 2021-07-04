arr = [2, 3, 1, 4, 5, 9, 10]

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left_arr = mergeSort(arr[0:mid])
        right_arr = mergeSort(arr[mid:])

        print(left_arr, right_arr)

        l = r = 0
        mergedArr = []

        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                mergedArr.append(left_arr[l])
                l += 1
            else:
                mergedArr.append(right_arr[r])
                r += 1
        mergedArr += left_arr[l:]
        mergedArr += right_arr[r:]
        return mergedArr


print(mergeSort(arr))