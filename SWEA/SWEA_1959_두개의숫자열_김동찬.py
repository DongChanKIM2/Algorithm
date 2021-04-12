t = int(input())
for tc in range(t):
    a, b = list(map(int, input().split()))
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    length = 0
    if a > b:
        length = a - b
    else:
        length = b - a
    # print(abs_length_dif)
    total = 0
    temp = 0

    if len(a_arr) < len(b_arr):
        for j in range(0, length+1):
            temp = 0
            for i in range(len(a_arr)):
                temp += a_arr[i]*b_arr[i+j]
            if temp > total:
                total = temp
    else:
        for j in range(0, length+1):
            temp = 0
            for i in range(len(b_arr)):
                temp += a_arr[i+j]*b_arr[i]
            if temp > total:
                total = temp

    print('#{} {}'.format(tc+1, total))