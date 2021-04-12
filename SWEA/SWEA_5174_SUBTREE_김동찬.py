# 전위 순회
def pretree(root):
    global cnt
    if root == 0:
        return
    else:
        # print(root)
        cnt += 1
        pretree(left[root])
        pretree(right[root])


t = int(input())
for tc in range(t):
    # 매 test case 마다 cnt 초기화
    cnt = 0
    # 간선개수, root
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (e+2)
    right = [0] * (e+2)
    # 출발 노드 기준으로
    for i in range(0, len(arr), 2):
        if left[arr[i]]:
            right[arr[i]] = arr[i+1]
        else:
            left[arr[i]] = arr[i+1]
    # print(left)
    # print(right)
    pretree(n)
    print('#{} {}'.format(tc+1, cnt))
