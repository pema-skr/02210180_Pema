class CustomList:
    def __init__(self, capacity=10):  # Fixed __init__ method
        """Initialize the list with a given capacity."""
        self._capacity = capacity
        self._size = 0
        self._array = [None] * self._capacity
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")

    def append(self, element):
        """Add an element to the end of the list."""
        if self._size == self._capacity:
            self._resize()
        self._array[self._size] = element
        self._size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        """Retrieve an element at a specific index."""
        if 0 <= index < self._size:
            return self._array[index]
        else:
            raise IndexError("Index out of range")

    def set(self, index, element):
        """Replace an element at a specific index."""
        if 0 <= index < self._size:
            self._array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            raise IndexError("Index out of range")

    def size(self):
        """Return the current number of elements in the list."""
        return self._size

    def _resize(self):
        """Resize the internal array when capacity is exceeded."""
        self._capacity *= 2
        new_array = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        print(f"Resized list to new capacity: {self._capacity}")

# Example usage:
cl = CustomList()  # Now the constructor works
cl.append(5)
print(f"Element at index 0: {cl.get(0)}")
cl.set(0, 10)
print(f"Element at index 0: {cl.get(0)}")
print(f"Current size: {cl.size()}")
