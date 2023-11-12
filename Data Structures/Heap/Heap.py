# What applies to trees also applies to heaps

# What is a Binary Heap?
#  - A tree sturcture similar to a binary search tree
#  - No order with left or with right
#  - Takes the least amount of space possible
#  - with the left side having priority of being filled before the right
#  - No implied ordering between siblings

# Finding a child node
# For any index of N in an array/collection/list
# The left child is stored at 2n+1
# The right child is stored at 2n+2

# Finding a parent node
# For any child node at index of N
# parent =  math.floor((n-1)/2)


# Max Binary heap
#  - Parents are always larger than children nodes
# Min Binary Heap
#  - Parents are always smaller than children nodes

# Big O
# insertion - O(log N)
# Removal - O(log N)
# Search - O(N)


import math
from typing import List


class Max_Binary_Heap:

    def __init__(self) -> None:
        self.values: List[int] = [41, 39, 33, 18, 27, 12]

    def insert(self, value):
        self.values.append(value)
        self.bubble()

    def bubble(self):
        index = len(self.values) - 1
        element = self.values[index]

        while index > 0:
            parent_index = math.floor((index - 1) / 2)
            parent = self.values[parent_index]
            if element <= parent:
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
            left_child = None
            right_child = None
            swap = None

            if left_index < length:
                left_child = self.values[left_index]
                if left_child > element:
                    swap = left_index

            if right_index < length:
                right_child = self.values[right_index]
                if swap is None and right_child > element:
                    swap = right_index
                elif (swap is not None and
                      (right_child and left_child) and
                      (right_child > left_child)):
                    swap = right_index

            if swap is None:
                break
            self.values[index] = self.values[swap]
            self.values[swap] = element
            index = swap

    def extract_max(self):
        Max = self.values[0]
        End = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = End
            self.bubble_down()
        return Max

    def get_values(self):
        print(self.values)


heap = Max_Binary_Heap()
heap.insert(55)

heap.get_values()
heap.extract_max()
heap.get_values()
