# Doubly Linked Lists
# Unlike Singly each node points to the previous node

# Drawback
#  Uses more memory


# BIG O
# INSERTION O(1)
# REMOVAL O(1)
# Searching O(N)
# Access O(N)

# Mostly used in something like a browser history where you go back or forward


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next: Node | None = None
        self.prev: Node | None = None


class Doubly_Linked_List:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length = 0

    def push(self, val):
        item = Node(val)

        if not self.head:
            self.head = item
            self.tail = item
        else:
            if self.tail:
                self.tail.next = item
                item.prev = self.tail
                self.tail = item
        self.length += 1
        return item

    def pop(self):
        if not self.head:
            return False
        if self.length == 1:
            temp = self.head
            self.tail = None
            self.head = None
            self.length -= 1
            return temp
        else:
            temp = self.tail
            if self.tail:
                self.tail = self.tail.prev
                if self.tail:
                    self.tail.next = None
            self.length -= 1
            return temp

    def shift(self):
        if self.length == 0:
            return False
        if self.length == 1:
            self.pop()
        else:
            temp = self.head
            if self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            self.length -= 1
            return temp

    def unshift(self, val):
        item = Node(val)
        if self.length == 0:
            self.push(val)
        else:
            if self.head:
                self.head.prev = item
                item.next = self.head
                self.head = item
        self.length += 1
        return item

    def get(self, val):
        if val < 0 or val >= self.length:
            return False
        if val <= self.length/2:
            count = 0
            current = self.head
            while count != val:
                if current:
                    current = current.next
                count += 1
            return current
        else:
            count = self.length-1
            current = self.tail
            while count != val:
                if current:
                    current = current.prev
                count -= 1
            return current

    def set(self, index, val):
        item = self.get(index)
        if item:
            item.val = val
            return True
        else:
            return False

    def insert(self, index, val):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.unshift(val)
            return True

        if index == self.length:
            self.push(val)
            return True

        else:
            item = Node(val)
            before = self.get(index-1)
            if before:
                after = before.next
                before.next = item
                if after:
                    item.next = after
                    item.prev = before
                    after.prev = item
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()
        else:
            item = self.get(index)
            if item:
                before_item = item.prev
                after_item = item.next
                if before_item:
                    before_item.next = after_item
                if after_item:
                    after_item.prev = before_item
                item.prev = None
                item.next = None
            return item

    def traverse(self):
        current = self.head
        # while current:
        #     print(f'{current.val}', end=',')

        while current:
            if current.prev:
                print(f'Prev: {current.prev.val}, ', end=' ')
            else:
                print('Prev: None', end=' ')
            print(f'Val: {current.val}', end='')
            if current.next:
                print(f', Next: {current.next.val}')
            else:
                print('  Next: None')

            current = current.next


list = Doubly_Linked_List()
list.push('1')
list.push('2')
list.push('3')
list.push('4')
list.push('5')
list.push('6')
list.push('7')
list.push('8')
list.push('9')
list.push('10')


# print(list.get(2).val)
print(list.remove(2))
# list.traverse()
list.traverse()
