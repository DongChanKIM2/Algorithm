str_arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
str_num_dict = {}  # 각 단어가 의미하는 값
for idx, s in enumerate(str_arr):
    str_num_dict[s] = idx

for tc in range(int(input())):
    count_arr = [0] * 10  # 각 단어가 나온 횟수
    temp = input().split()
    n = int(temp[1])  # 단어 개수
    input_arr = input().split()
    # 단어 등장 횟수 각각 기록
    for word in input_arr:
        count_arr[str_num_dict[word]] += 1

    answer_arr = []  # 최종 반환 문자열
    for i in range(10):
        word = str_arr[i]
        count = count_arr[i]
        # answer_arr.extend([word] * count)
        # answer_arr.extend([str_arr[i]] * count_arr[i])
        answer_arr.append(str_arr[i] * count_arr[i])

    print('#{}'.format(tc + 1))
    print(' '.join(answer_arr))