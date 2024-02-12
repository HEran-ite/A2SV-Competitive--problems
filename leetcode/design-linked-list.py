class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        curr = self.head
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        else:
            count = 0
            curr = self.head
            while curr:
                if count == index - 1:
                    new_node = Node(val)
                    new_node.next = curr.next
                    curr.next = new_node
                    return
                curr = curr.next
                count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        curr = self.head
        while curr:
            if count + 1 == index:      
                if curr.next:
                    curr.next = curr.next.next
                return
            curr = curr.next
            count += 1