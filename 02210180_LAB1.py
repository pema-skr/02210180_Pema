class CustomList:
    def __init__(self, capacity=10):
        """Initialize the list with a given capacity."""
        self._capacity = capacity  # Maximum number of elements before resizing
        self._size = 0  # Number of elements currently in the list.
        self._array = [None] * self._capacity  # Private array to store elements
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")

    def append(self, element):
        """Add an element to the end of the list."""
        if self._size == self._capacity:
            self._resize()  # Increase capacity if needed
        self._array[self._size] = element  # Store the element in the array
        self._size += 1  # Increase the size
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
        self._capacity *= 2  # Double the capacity
        new_array = [None] * self._capacity  # Create a new larger array
        for i in range(self._size):  # Copy elements to the new array
            new_array[i] = self._array[i]
        self._array = new_array  # Replace the old array with the new one
        print(f"Resized list to new capacity: {self._capacity}")

cl = CustomList()  # Create an instance of CustomList

cl.append(5)  # Add element 5 to the list
print(f"Element at index 0: {cl.get(0)}")  # Retrieve element at index 0

cl.set(0, 10)  # Replace element at index 0 with 10
print(f"Element at index 0: {cl.get(0)}")  # Retrieve the updated element

print(f"Current size: {cl.size()}")  # Check the current size of the list
