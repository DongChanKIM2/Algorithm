# 1. 목표: Node를 활용해 단방향(singly linked list) 전체 구현
# 2. 준비물
# 참조 사이트: https://www.youtube.com/watch?v=p4tIvWIS_SE

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 리스트 Print 할 수 있는 두 가지 방법
# 1. iterative
def printNodes(node: ListNode):
    current_node = node
    # while current_node is not None:
    while current_node:
        print(current_node.val, end=' ')
        current_node = current_node.next


# printNodes(head_node)


class SLinkedList:
    # 아무 정보 없는 Head Node 생성
    def __init__(self):
        self.head = None

    # 시간복잡도: O(1)
    # Head Node 에다 새로운 Node 연결하는 함수
    def addAtHead(self, val):
        # 1. 숫자가 들어있는 Node 하나 생성
        node = ListNode(val)
        # 2. head가 가르키는 방향에다가 생성한 Node의 next를 줌
        node.next = self.head
        # 3. head를 Node에 연결
        self.head = node

    # 시간복잡도: O(n)
    # bug: Slinkedlist에 아무런 Node가 없다면 작동하지 않음
    def addBack(self, val):
        # 노드 생성
        node = ListNode(val)
        # head 가 현재 Node
        current_node = self.head
        # 갈 수 잇을 때까지 교체하고
        while current_node.next:
            current_node = current_node.next
        # 끝에 node 에다가 만들어준 node 추가해주기
        current_node.next = node

    # 시간복잡도: O(1) ~ O(N)
    def findNode(self, val):
        current_node = self.head
        while current_node:
            if current_node.val == val:
                return current_node
            current_node = current_node.next
        raise RuntimeError('Node Not Found')

    # 시간복잡도: O(1)
    # 인자 node 다음에다가 추가해주기
    def addAfter(self, node, val):
        # 추가해줄 새로운 Node 생성
        new_node = ListNode(val)
        # 우선 기존의 1이 가르키고 있는 3을 새로 만들어준 Node도 가르키게 만들고
        new_node.next = node.next
        # 기존의 1이 가르키는 걸 3에서 새로 추가해준 4로 변경
        node.next = new_node

    # 시간복잡도: O(1)
    # prev_node.next를 삭제하는 함수로 파이썬과 같은 managed 언어에서는 자동 삭제가 되지만
    # c와 같은 언어에서는 별도의 삭제처리가 필요함
    def deleteAfter(self, prev_node):
        if prev_node.next:
            prev_node.next = prev_node.next.next


sList = SLinkedList()
sList.addAtHead(1)
sList.addAtHead(2)
sList.addBack(3)


# 숫자 1을 반환한게 아니라 숫자1을 가지고 있는 node를 반환했으므로 next도 가지고 있음!!
node1 = sList.findNode(1)
# node2 = sList.findNode(4)
sList.addAfter(node1, 4)
printNodes(sList.head)
