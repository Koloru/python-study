# What is a "Singly Linked List"
# - Data structure that stores
# - Is ordered
# - Contains a Head, Tail and Length
# - No indexes. Only has nodes that point to the next element
# - Each node has a value and a pointer to another node or null
# Random accessing is also not allowed
# to get to a value you have to start from the beginning to end

# Nodes
# - Each element is a node
# - A node stores a piece of data
# - Nodes reference the next node


# Advantages
# Goot at insertion and deletion
from typing import Any


class Node:
    def __init__(self, val) -> None:
        self.val: Any | None = val
        self.next: Node | None = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: None | Node = None
        self.tail: None | Node = None
        self.length: int = 0

    def push(self, value):
        item = Node(value)
        if not self.head:
            self.head = item
            self.tail = self.head
        else:
            assert self.tail is not None
            self.tail.next = item
            self.tail = item
        self.length += 1

    def pop(self):
        if not self.head:
            self.length = 0
            return

        if not self.head.next:
            val = self.head.val
            self.head = None
            self.tail = None
            self.length -= 1
            return val

        current = self.head
        temp = current
        while current.next:
            temp = current
            current = current.next
        val = current
        self.tail = temp
        self.tail.next = None
        self.length -= 1
        return current.val

    def shift(self):
        if not self.head:
            self.length = 0
            return

        if not self.head.next:
            val = self.head.val
            self.head = None
            self.tail = None
            self.length -= 1
            return val

        old_head = self.head
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return old_head

    def traverse(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.val)
            curr = curr.next
        print(elements)


data = SinglyLinkedList()
data.push('hello')
data.push('there')
data.push('mr')
data.push('jones')
# data.traverse()

data.shift()


data.traverse()
