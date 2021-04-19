# 우선 한 개가 될 때까지 쪼개는 역할만 해주는 divide 함수
def divide(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[0:mid]
    right_arr = arr[mid:len(arr)]
    left_arr = divide(left_arr)
    right_arr = divide(right_arr)
    return merge(left_arr, right_arr)


# divide 함수에서 받아온 return값들을 merge의 파라미터로 input으로 주자
# 크기대로 정렬하면서 합치는게 merge 함수의 역할
def merge(left_arr, right_arr):
    global cnt
    if left_arr[-1] > right_arr[-1]:
        cnt += 1
    # 아직 헷갈리는 부분 divide하고 들어오면 초기화 되는게 아닌가?? 다시 생각좀해봐야겟따...
    result = []
    # 왼쪽, 오른쪽 중 남아있는 값이 하나라도 있으면 실행 유지
    while len(left_arr) > 0 or len(right_arr) > 0:
        # 둘 다 값이 남아 있다면 작은거부터 넣어주자(왼쪽, 오른쪽 중)
        if len(left_arr) > 0 and len(right_arr) > 0:
            if left_arr[0] <= right_arr[0]:
                result.append(left_arr[0])
                left_arr = left_arr[1:]
            else:
                result.append(right_arr[0])
                right_arr = right_arr[1:]
        elif len(left_arr) > 0:
            result.append(left_arr[0])
            left_arr = left_arr[1:]
        elif len(right_arr) > 0:
            result.append(right_arr[0])
            right_arr = right_arr[1:]
    return result


t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = divide(arr)
    print('#{} {} {}'.format(tc+1, result[n//2], cnt))
