# A simple implementation of ArrayList(also known as a dynamic array).
# The key feature demonstrated: Automatic resizing when capacity is exceeded.
# Dynamic insert/remove with element shifting.
# Custom get() and set() methods for safe access, Internal capacity tracking(as in Java ArrayList).

class Arraylist:
    def __init__(self):
        self._capacity = 4 # Initial fixed size.
        self._size = 0
        self._data = [None] * self._capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data    
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(self._ *  2)   # double the capacity
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                for j in range(i, self._size - 1):
                    self._data[j] = self._data[j + 1]
                self._data[self._size - 1] == None
                self._size -= 1
                return

        raise ValueError("Value not found in list") 

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index put of bound")
        return self._data[index]
    
    def set(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        self._data[index] = value

    def size(self):
        return self._size
    
    def capacity(self):
        return self._capacity
    
    def __str__(self):
        return "[" + ", ".join(repr(self._data[i]) for i in range(self._size)) + "]"
    
# Example usage:

if __name__ == "__main__":    
    alist = Arraylist()
    alist.append(10)
    alist.append(20)
    alist.append(30)
    alist.insert(1, 15)
    print(alist)
    alist.remove(20)
    print(alist)
    print("Element at index 1:", alist.get(1))
    print("size:", alist.size())
    print("Capacity:", alist.capacity())








