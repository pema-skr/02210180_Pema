#: Implement the Node and List Class Structure,Implement Basic Operations
class Node:
    """A class representing a node in a linked list."""

    def __init__(self, data):
        """Initialize a node with data and a reference to the next node."""
        self.data = data  # Store the element
        self.next = None  # Initially, the next reference is set to None


class LinkedList:
    """A class representing a linked list data structure with various operations."""

    def __init__(self):
        """Initialize an empty linked list with head, tail, and size."""
        self.head = None  # Head reference to the first node
        self.tail = None  # Tail reference to the last node (optional but useful)
        self.size = 0  # Counter to track the number of elements in the list
        print("Created new LinkedList")
        print("Current size:", self.size)
        print("Head:", self.head)

    def append(self, element):
        """Add an element to the end of the list."""
        new_node = Node(element)  # Create a new node
        if self.head is None:
            self.head = new_node  # If list is empty, set new node as head
            self.tail = new_node  # Also set it as tail
        else:
            self.tail.next = new_node  # Link last node to new node
            self.tail = new_node  # Update tail reference
        self.size += 1  # Increase size counter
        print(f"Appended {element} to the list")

    def get(self, index):
        """Retrieve an element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next  # Move to next node
        return current.data

    def set(self, index, element):
        """Replace an element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next  # Move to next node
        current.data = element
        print(f"Set element at index {index} to {element}")

    def size(self):
        """Return the current number of elements in the list."""
        return self.size

    def prepend(self, element):
        """Add an element at the beginning of the list."""
        new_node = Node(element)
        new_node.next = self.head  # New node points to old head
        self.head = new_node  # Update head reference
        if self.tail is None:
            self.tail = new_node  # If list was empty, update tail
        self.size += 1
        print(f"Prepended {element} to the list")

    def print_list(self):
        """Print all elements in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked list:", elements)


# Example usage
test_list = LinkedList()
test_list.append(5)

print("Element at index 0:", test_list.get(0))
test_list.set(0, 10)
test_list.prepend(12)
test_list.prepend(16)
test_list.prepend(18)

print("Element at index 2:", test_list.get(2))
print("Current size:", test_list.size)
test_list.print_list()
