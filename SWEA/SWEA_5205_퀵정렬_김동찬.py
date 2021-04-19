# 매번 리스트를 생성하면 시간초과 나서 새로운 quick 정렬 함수
# 새로운 리스트를 만드는 게 아니라 내부에서 정렬해보자
# sort가 범위를 나눠서 partition에 전달해주면 정렬해서 sort에 돌려줌


def quick(arr):
    def sort(low, high):
        # low=0 high=마지막 idx
        # 겹치는 순간이 오면 return
        if high <= low:
            return

        # partition의 low값을 mid에 매칭
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)
        return arr

    def partition(low, high):
        # 중간점을 pivot 으로 설정
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)


t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = quick(arr)
    print('#{} {}'.format(tc+1, result[n//2]))
