# Trees

# ---------- TYPES ----------
# Trees, Binary Trees, Binary Search Trees
# Trees - Can have many children
# Binary Tree - Each node can have at most 2 children
# Binary Search Tree - Sorted Binary Tree
#  - children to the left of BSTs are lower than the children on the right
#       42
# 31       43


# Trees consists of nodes that are in a parent / child relationship
# Trees are non-linear(They can have more than one pathway)
# Top most node is called the "ROOT"
# Can reference 0 or more nodes

# Terminology
# ROOT - TOP NODE IN THE TREE
# CHILD - NODE DIRECTLY CONNECTED TO ANOTHER NODE WHEN MOVING AWAY FROM THE ROOT
# PARENT - The converse notion of a child
# Sibling -  A group of nodes with the same parent
# Leaf - A node with no children
# Edge - connection between a node

# Rules for trees
# A node can only point to a child node.
# - a node cannot point to a sibling or a parent
# - a tree cannot have more than 1 root
# - a node cannot have more than 1 parent


# Uses for trees
# HTML DOM
# Network Routing
# Abstract Syntax Tree
# Artificial intelligence
# Folders in operating system

# BIG O Trees
# insertion - O(log n)
# searching - O(log n)


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


tree = Binary_Search_Tree()
values = [5, 3, 7, 2, 4, 6, 8]

for value in values:
    tree.insert(value)

tree.insert(4)
tree.insert(4)
tree.insert(4)
tree.insert(4)
tree.insert(4)
tree.insert(4)
tree.insert(4)
tree.insert(4)
tree.display(tree.root)
