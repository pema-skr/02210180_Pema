# Filename: 02210180_LAB7.py
#Task1
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)
            print(f"Created new Binary Tree\nRoot: {self.root.value}")
        else:
            self.root = None
            print(f"Created new Binary Tree\nRoot: None")

if __name__ == "__main__":
    tree = BinaryTree()  # Creates an empty tree

#Task2
# Filename: 02210180_LAB7.py

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)
            print(f"Created new Binary Tree\nRoot: {self.root.value}")
        else:
            self.root = None
            print(f"Created new Binary Tree\nRoot: None")

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def is_full_binary_tree(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left and node.right:
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    def is_complete_binary_tree(self):
        if self.root is None:
            return True
        queue = []
        queue.append(self.root)
        encountered_none = False

        while queue:
            current = queue.pop(0)
            if current:
                if encountered_none:
                    return False
                queue.append(current.left)
                queue.append(current.right)
            else:
                encountered_none = True
        return True

# --- Example usage ---
if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(f"Tree Height: {tree.height(tree.root)}")
    print(f"Total Nodes: {tree.size(tree.root)}")
    print(f"Leaf Nodes Count: {tree.count_leaves(tree.root)}")
    print(f"Is Full Binary Tree: {tree.is_full_binary_tree()}")
    print(f"Is Complete Binary Tree: {tree.is_complete_binary_tree()}")
