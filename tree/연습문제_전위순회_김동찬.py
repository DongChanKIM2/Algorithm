# 방문한 노드의 번호를 출력
# 전위순회
# tc : 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13


def preorder(root):
    if root == 0:
        return
    else:
        print(root, end=' ')
        preorder(left[root])
        preorder(right[root])


# 중위순회
def inorder(root):
    if root == 0:
        return
    else:
        inorder(left[root])
        print(root, end=' ')
        inorder(right[root])


# 후위순회
def postorder(root):
    if root == 0:
        return
    else:
        postorder(left[root])
        postorder(right[root])
        print(root, end=' ')


n = int(input())
arr = list(map(int, input().split()))
# 1부터 n+1까지이니까 0을 고려하면 n+2개 길이 생성
left = [0] * (n+2)
right = [0] * (n+2)
# 시작점 기준
for i in range(0, len(arr), 2):
    papa, baby = arr[i], arr[i+1]
    if left[papa]:
        right[papa] = baby
    else:
        left[papa] = baby

print(left)
print(right)
preorder(2)
print()
inorder(1)
print()
postorder(1)
