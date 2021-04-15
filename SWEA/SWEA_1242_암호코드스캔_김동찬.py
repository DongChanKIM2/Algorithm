hex_dictionary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                  '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                  '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                  'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
                  }

decode = {'211': 0, '221': 1, '122': 2, '411': 3,
          '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}


def HexaToBin(temp):
    global binary
    for hex_i in temp:
        binary += hex_dictionary[hex_i]
    return binary


def minimumchk(x, y, z):
    global a
    global b
    global c
    minimum = min(x, y, z)
    x //= minimum
    y //= minimum
    z //= minimum
    a, b, c = x, y, z
    return a, b, c


def anscheck(result):
    if ((result[0] + result[2] + result[4] + result[6]) * 3 + (result[1] + result[3] + result[5] + result[7])) % 10 == 0:
        return sum(result)
    else:
        return False


import sys
sys.stdin = open("input.txt")

# 전체풀이 흐름:
# 1. 행마다 조회를 하고 중복되는 행이면 pass하고 아니면 추가
# 2. 추가된 행에서 16진수 -> 2진수로 변현해주기
# 3. 변환된 2진수행에서 중복되는 비밀번호는 pass하고 아니면 추가
# 4. 추가된 2진수를 비밀번호 유효성 검사를 해서 맞으면 최종결과에 더해주기


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(n)]
    temp = []
    # 중복되지 않은 16진수 행
    temp_all = []
    # 이진수로 변환한 숫자 모두 담는 거
    binary_all = []
    # 비밀번호(십진수) 담는 거
    result_all = []
    # 출력하는 정답
    maximum_result = 0

    for idx in range(n):
        temp = arr[idx]
        # 중복된 행이면 skip 하자
        if temp in temp_all:
            continue
        # 처음이면 추가해서 검사해주자
        else:
            temp_all.append(temp)
            binary = ''
            HexaToBin(temp)

        # 암호가 같은거면 skip
        if binary in binary_all:
            continue
        # 처음보는 암호면 추가해서 검사
        else:
            binary_all.append(binary)
            binary = list(map(int, binary))

            result = []
            # 1, 0, 1 암호 개수 판별
            a, b, c = 0, 0, 0
            # 암호가 끝에서부터 처음으로 돌아가면서 개수 counting
            for i in range(len(binary)-1, -1, -1):

                if a == 0 and b == 0 and binary[i] == 1:
                    c += 1
                elif c > 0 and a == 0 and binary[i] == 0:
                    b += 1
                elif b > 0 and c > 0 and binary[i] == 1:
                    a += 1
                # 암호라고 판별이 된다면
                if a > 0 and b > 0 and c > 0 and binary[i] == 0:
                    # 최소 비율로 맞추기
                    minimumchk(a, b, c)
                    everything = str(a) + str(b) + str(c)
                    # result(암호)에 추가해주고 초기하해주기
                    if everything in decode:
                        result.append(decode[everything])
                        a, b, c = 0, 0, 0
                # print(result)
                # print('-------')
                # print(result_all)
                # result(암호)가 8개가 된다면
                if len(result) == 8:
                    # print(result)
                    # 차례대로 append 해줬으니까 역순처리 해줘야함
                    result.reverse()
                    if result in result_all:
                        result = []
                        # continue해줘도 초기화해줘야지 바보야!!!!!!!!!!!!
                        continue
                    else:
                        result_all.append(result)
                        # 유효한 비밀번호라면 최종값이 maximum result 에 합을 더해주자
                        if anscheck(result):
                            maximum_result += sum(result)
                    result = []

    if maximum_result:
        print('#{} {}'.format(tc+1, maximum_result))
    else:
        print('#{} {}'.format(tc+1, 0))


