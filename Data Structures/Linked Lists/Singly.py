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


# BIG O
# Advantages
# Goot at insertion and deletion at the beginning and at the end

# Insertion O(1) when adding to the end of beginning
# O(N) when inserting in the middle of the list

# Removal
# O(1) at the start
# Pop() O(n)

# Searching
# O(n)

# Accessing
# O(n)


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

    def unshift(self, val):
        item = Node(val)
        if not self.head:
            self.head = item
            self.tail = self.head
        else:
            item.next = self.head
            self.head = item
        self.length += 1
        return item

    def get(self, val):
        if val < 0 or val >= self.length:
            return None
        counter = 0
        current = self.head
        while counter != val:
            if current:
                current = current.next
            counter += 1
        if current:
            return current

    def set(self, index, val):
        item = self.get(index)
        if item:
            item.val = val
            return True
        return False

    def insert(self, index, val):
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            self.push(val)
        if index == 0:
            self.unshift(val)
        else:
            item = self.get(index-1)
            new_node = Node(val)
            if item:
                new_node.next = self.get(index)
                item.next = new_node
                self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == self.length-1:
            self.pop()
        if index == 0:
            self.shift()

        prev = self.get(index-1)
        if prev and prev.next:
            prev.next = prev.next.next
            self.length -= 1

    def traverse(self):
        current = self.head
        while current:
            print(current.val, end=' ')
            current = current.next

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        prev = None
        next = None

        counter = 0
        while counter < self.length:
            if node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            counter += 1
        return

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


print(data.reverse())
# print(data.get(0))
# print(data.length)
# print(data.remove(0))
print(data.traverse())
print(data.traverse())
