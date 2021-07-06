arr = [4, 2, 1, 3, 9, 4]

def quicksort(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        pivot = arr[mid]
        less, equal, more = [], [], []
        for _ in range(len(arr)):
            each = arr.pop()
            if each < pivot:
                less.append(each)
            elif each > pivot:
                more.append(each)
            else:
                equal.append(each)
        return quicksort(less) + equal + quicksort(more)


# 메모리절약 ver
def partition(arr, start, end):
    pivot = arr[(start+end)//2]
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return start



def quicksort2(arr, start, end):
    pivot = partition(arr, start, end)
    if start < pivot - 1:
        quicksort2(arr, start, pivot-1)
    if pivot < end:
        quicksort2(arr, pivot, end)
    return arr


# print(quicksort(arr))
print(quicksort2(arr, 0, 5))

