# YourStudentNo_LAB9.py
# LAB 8 – Part 2: Red-Black Tree
# Implemented by: 02210167 Jigme Choden Ghalley
# Partner: 02210180 Pema TChecki 

# Partner 2: Red-Black Tree implementation

RED = True
BLACK = False

class Node:
    def __init__(self, data):
        self.data = data
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = BLACK
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = RED
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)

        self.root.color = BLACK

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if node == self.NIL or value == node.data:
            return node != self.NIL
        if value < node.data:
            return self._search_tree(node.left, value)
        return self._search_tree(node.right, value)

    def get_black_height(self):
        node = self.root
        height = 0
        while node != self.NIL:
            if node.color == BLACK:
                height += 1
            node = node.left
        return height

    def print_tree(self, node=None, indent="", last=True):
        if node is None:
            node = self.root
        if node != self.NIL:
            print(indent, "`- " if last else "|- ", f"{node.data} ({'B' if node.color == BLACK else 'R'})", sep="")
            indent += "   " if last else "|  "
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

# Example usage:
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    rb_tree.insert(10)
    rb_tree.insert(20)
    rb_tree.insert(30)
    rb_tree.insert(15)
    rb_tree.insert(25)

    print("Red-Black Tree:")
    rb_tree.print_tree()

    print("Search 15:", rb_tree.search(15))
    print("Black Height:", rb_tree.get_black_height())
