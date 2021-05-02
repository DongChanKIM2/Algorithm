# 1. 목표: 단방향(singly linked list) 준비물의 Node 생성 및 출력
# 2. 준비물
# 2.1 Node structure: val(값), 위치표시(next)


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# val: 1만 주고 next(다음 위치)는 없는 상태의 머리(head) Node 생성
head_node = ListNode(1)
# print(head_node.val)
# print(head_node.next)
# val: 2인 새로운 Node 를 가르키기
head_node.next = ListNode(2)
# val: 3인 새로운 Node 를 가르키기
head_node.next.next = ListNode(3)
# val: 4인 새로운 Node 를 가르키기
head_node.next.next.next = ListNode(4)


# 리스트 Print 할 수 있는 두 가지 방법
# 1. iterative
def printNodes(node: ListNode):
    current_node = node
    # while current_node is not None:
    while current_node:
        print(current_node.val, end=' ')
        current_node = current_node.next


# printNodes(head_node)

# 2. Recursive
def printNodesRecur(node: ListNode):
    print(node.val, end=' ')
    if node.next:
        printNodesRecur(node.next)


printNodesRecur(head_node)