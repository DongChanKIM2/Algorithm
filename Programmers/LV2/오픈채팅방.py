# 프로그래머스와 백준의 차이점
# 1. 함수안에 들어오는 인자가 배열임!!(문자열들로 이루어진 배열)
# 2. 파이참에서 돌리는 것보다 채점사이트에서 돌리는게 더 직관적임..
# 3. 여러 문제를 풀어보면서 적응해야 할듯


def solution(record):
    answer = []
    user_dict = {}
    for mes in record:
        if mes.split(' ')[0] == 'Enter' or mes.split(' ')[0] == 'Change':
            user_dict[mes.split(' ')[1]] = mes.split(' ')[2]
    for mes in record:
        temp = ''
        if mes.split(' ')[0] == 'Enter':
            temp += user_dict[mes.split(' ')[1]] +'님이 들어왔습니다.'
        elif mes.split(' ')[0] == 'Leave':
            temp += user_dict[mes.split(' ')[1]] +'님이 나갔습니다.'
        else:
            continue
        answer.append(temp)
    return answer
