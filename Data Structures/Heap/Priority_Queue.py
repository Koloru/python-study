import math
from typing import List


class Node:
    def __init__(self, value, priority) -> None:
        self.value = value
        self.priority: int = priority


class Priority:
    def __init__(self) -> None:
        self.values: List[Node] = []

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        self.values.append(new_node)
        self.bubble()

    def bubble(self):
        index = len(self.values) - 1
        element = self.values[index]

        while index > 0:
            parent_index = math.floor((index - 1) / 2)
            parent = self.values[parent_index]
            if element.priority >= parent.priority:
                break
            self.values[parent_index] = element
            self.values[index] = parent
            index = parent_index

    def bubble_down(self):
        index = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            left_child: None | Node = None
            right_child: None | Node = None
            swap = None

            if left_index < length:
                left_child = self.values[left_index]
                if left_child.priority < element.priority:
                    swap = left_index

            if right_index < length:
                right_child = self.values[right_index]
                if (
                    (swap is None and right_child.priority < element.priority)
                    or
                    (swap is not None and right_child and left_child and
                     right_child.priority < left_child.priority)
                ):
                    swap = right_index

            if swap is None:
                break
            self.values[index] = self.values[swap]
            self.values[swap] = element
            index = swap

    def dequeue(self):
        Max = self.values[0]
        End = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = End
            self.bubble_down()
        return Max

    def get_values(self):
        for item in self.values:
            print(item.priority, item.value)


ER = Priority()
ER.enqueue("Cold", 5)
ER.enqueue("Dick", 4)
ER.enqueue("AA", 3)
ER.enqueue("REE", 2)
ER.enqueue("Covid", 1)
ER.enqueue("Gunshot", 9)
ER.get_values()
