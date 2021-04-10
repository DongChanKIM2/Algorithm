#1.
def SelectionSort(N, arr):
    for i in range(N):
        minimum_idx = i
        for j in range(i+1, len(arr)):
            if arr[minimum_idx] > arr[j]:
                minimum_idx = j
        arr[i], arr[minimum_idx] = arr[minimum_idx], arr[i]
    return arr


arr = [5, 2, 6, 1, 9, 3, 7, 8, 4]

print(SelectionSort(1, arr))

#2.
[2, 5, 6, 1, 9, 3, 7, 8, 4]
[1, 2, 6, 5, 9, 3, 7, 8, 4]
5보다 작은 minimum_idx가 처음으로 2가 있고 2보다 작은 수로는 1이 있으므로
위와 같이 2번 교환하게 된다.
실제로 swap하는 것은 N=1을 주었으므로 한 번 SWAP하게 된다.
