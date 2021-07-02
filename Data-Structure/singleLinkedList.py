def printNodes(node):
    crnt_node = node
    while crnt_node:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# head_node = ListNode(1)
# head_node.next = ListNode(2)
# head_node.next.next = ListNode(3)
#
# printNodes(head_node)

class SLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def addAtBack(self, val):
        node = ListNode(val)
        crnt_node = self.head
        while crnt_node.next:
            crnt_node = crnt_node.next
        crnt_node.next = node

    def findNode(self, val):
        crnt_node = self.head
        while crnt_node:
            if crnt_node.val == val:
                return crnt_node
            else:
                crnt_node = crnt_node.next

    def addAfter(self, node, val):
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node

    def deleteAfter(self, prev_node):
        if prev_node.next:
            prev_node.next = prev_node.next.next


slist = SLinkedList()
slist.addAtHead(1)
slist.addAtHead(2)
slist.addAtBack(3)
# printNodes(slist.head)

node1 = slist.findNode(1)
slist.addAfter(node1, 4)
slist.deleteAfter(node1)
printNodes(slist.head)

