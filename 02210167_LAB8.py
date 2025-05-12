class Node:
    def __init__(self, value, color='red'):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color  # 'red' or 'black'

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, 'black')  # Sentinel NIL node
        self.root = self.NIL
    
    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        
        parent = None
        current = self.root
        
        # Find the appropriate parent
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        
        # Fix the Red-Black Tree properties
        self._fix_insert(new_node)
    
    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    # Case 1: Uncle is red
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Uncle is black and node is right child
                        node = node.parent
                        self._left_rotate(node)
                    # Case 3: Uncle is black and node is left child
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    # Case 1: Uncle is red
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: Uncle is black and node is left child
                        node = node.parent
                        self._right_rotate(node)
                    # Case 3: Uncle is black and node is right child
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
        
        self.root.color = 'black'
    
    def _left_rotate(self, x):
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
    
    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        
        x.right = y
        y.parent = x
    
    def get_black_height(self):
        if self.root == self.NIL:
            return 0
        
        node = self.root
        black_height = 0
        
        while node != self.NIL:
            if node.color == 'black':
                black_height += 1
            node = node.left
        
        return black_height
    
    def print_tree(self):
        self._print_tree(self.root, "", True)
    
    def _print_tree(self, node, indent, last):
        if node != self.NIL:
            print(indent, end='')
            if last:
                print("R----", end='')
                indent += "     "
            else:
                print("L----", end='')
                indent += "|    "
            
            color = "RED" if node.color == 'red' else "BLACK"
            print(f"{node.value}({color})")
            self._print_tree(node.left, indent, False)
            self._print_tree(node.right, indent, True)


# Create and populate the Red-Black Tree
rb_tree = RedBlackTree()
values = [20, 10, 30, 5, 15, 25, 35]

for value in values:
    rb_tree.insert(value)

# Print the tree structure
print("Red-Black Tree Structure:")
rb_tree.print_tree()

# Get and print the black height
black_height = rb_tree.get_black_height()
print(f"\nBlack height of the tree: {black_height}")