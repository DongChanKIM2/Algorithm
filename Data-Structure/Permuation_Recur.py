arr = [1,2,3]
N = 3
# 사용할 결과물을 담을 변수(결과들이 저장될 리스트)
sel = [0] * N
# in_permutation 해당숫자를 썼는지 안썼는지에 대한 체크
check = [0] * N  # 해당 원소를 이미 사용했는지 안했는지에 대한 체크


def perm(idx):
    # 다 뽑아서 정리했다면
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            # 해당 원소가 사용이 되지 않았다면
            if check[i] == 0:
                sel[idx] = arr[i]  # 값을 써라
                check[i] = 1  # i번째 원소를 사용했다는 표시
                perm(idx+1)
                check[i] = 0  # 다음 반복문을 위한 원상복귀

perm(0)