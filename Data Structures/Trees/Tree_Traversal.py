# Tree Traversal
# (Given on any tree) (Works on any tree)

from typing import List

# Visit every node once
# Traversing a tree
# ----------------- MAIN APPROACHES -----------------
# Breadth-first Search
# Going across per row
# (visiting every sibling node in a row of nodes before going down)


def BFS(self):
    if not self.root:
        return
    data: List[Node] = []
    data_values = []
    queue = []
    node = self.root
    queue.append(self.root)
    while queue:
        node = queue.pop(0)
        data.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    for item in data:
        data_values.append(item.value)
    return data_values


# Depth-first Search
# Go vertically down to the last node to the right or to the left before going to a sibling node

# Types of DFS
# In Order DFS
def DFS_IN_ORDER(self):
    data = []
    current = self.root

    def traverse(node):
        if node.left:
            traverse(node.left)
        data.append(node.value)
        if node.right:
            traverse(node.right)

    traverse(current)
    return data

# Pre Order DFS


def DFS_PRE_ORDER(self):
    data = []
    current = self.root

    def traverse(node):
        data.append(node.value)
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)
    traverse(current)
    return data


# Post Order DFS
# Root is the last one visited in this order
def DFS_POST_ORDER(self):
    data = []
    current = self.root

    def traverse(node):
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)
        data.append(node.value)

    traverse(current)
    return data

# ----------------- When to use which -----------------
# The time complexity of both of these methods dont matter because you visit each node 1 time
# Meanwhile the space complexity of BFS compared to DFS is more if you have a very large tree
# If the tree is wide horitzontally and it doesnt have many children its better to use DFS
# if the tree is vertically large its better to use BFS because the queue doesnt get filled

# DFS use cases
# In Order - on a BST its "IN ORDER" from lowest to highest
# Pre order - useful if youre trying to clone/duplicate a tree
#
# End of the day its very easy to switch in between DFS' the main concern is when to use BFS or DFS


# Tree
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


class Binary_Search_Tree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value == current.value:
                    return False
                if value < current.value:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = new_node
                        break
                elif value > current.value:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = new_node
                        break

    def find(self, value):
        if not self.root:
            return False
        current = self.root
        found = False
        while not found and current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True
        if not found:
            return False
        return current

    def display_in_order(self, node):
        if node is not None:
            self.display_in_order(node.left)
            print(node.value)
            self.display_in_order(node.right)

    def display(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left is not None or node.right is not None:
                if node.left is not None and node.right is not None:
                    self.display(node.right, level + 1, "R: ")
                    self.display(node.left, level + 1, "L: ")
                elif node.right is not None:
                    self.display(node.right, level + 1, "R: ")
                else:
                    self.display(node.left, level + 1, "L: ")

    def BFS(self):
        if not self.root:
            return
        data: List[Node] = []
        data_values = []
        queue = []
        node = self.root
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            data.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        for item in data:
            data_values.append(item.value)
        return data_values

    def DFS_PRE_ORDER(self):
        data = []
        current = self.root

        def traverse(node):
            data.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(current)
        return data

    def DFS_POST_ORDER(self):
        data = []
        current = self.root

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            data.append(node.value)

        traverse(current)
        return data

    def DFS_IN_ORDER(self):
        data = []
        current = self.root

        def traverse(node):
            if node.left:
                traverse(node.left)
            data.append(node.value)
            if node.right:
                traverse(node.right)

        traverse(current)
        return data


tree = Binary_Search_Tree()
# values = [5, 3, 7, 2, 4, 6, 8]
values = [10, 6, 15, 3, 8, 20]

for value in values:
    tree.insert(value)

print(tree.DFS_PRE_ORDER())
print(tree.DFS_POST_ORDER())
print(tree.DFS_IN_ORDER())
