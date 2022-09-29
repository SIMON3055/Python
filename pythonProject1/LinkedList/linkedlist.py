class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print(self):
        temp = self.head
        while temp.next:
            print(temp.data,end="->")
            temp = temp.next
        print(temp.data)

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        return prev


l1 = Node(5)
l1.next = Node(4)
l1.next.next = Node(8)
l1.next.next.next = Node(2)

LinkedList(l1).print()
l2 = LinkedList(l1).reverse()
LinkedList(l2).print()

