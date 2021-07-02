def solution(progresses, speeds):
    answer = []
    # print(progresses, speeds)
    while True:
        # print(progresses, answer)
        temp = 0
        if sum(answer) == len(progresses):
            break
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                continue
            else:
                progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if progresses[i] < 100:
                break
            elif progresses[i] == 99999999:
                continue
            elif progresses[i] >= 100:
                progresses[i] = 99999999
                temp += 1
        if temp:
            answer.append(temp)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
