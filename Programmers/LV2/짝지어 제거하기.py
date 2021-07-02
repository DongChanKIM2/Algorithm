def solution(s):
    answer = -1
    s_lst = list(s)
    temp = []
    for i in range(len(s_lst)):
        temp.append(s_lst[i])
        if len(temp) >= 2:
            if temp[-1] == temp[-2]:
                temp.pop()
                temp.pop()
    if len(temp) == 0:
        answer = 1
    else:
        answer = 0

    return answer


print(solution('baabaa'))
print(solution('cdcd'))