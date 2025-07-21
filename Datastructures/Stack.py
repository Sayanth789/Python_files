# This is an implemetation of stack in python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item into the stack."""   
        self.items.append(item)
    def pop(self, item):
        """Popping an item from the stack.""" 
        if self.is_empty():
            raise IndexError("Remove and return an item from stack. Raise IndexError if it is empty.")
        return  self.items.pop   
    def peek(self, item):
        """Return an item without removing it"""
        if self.is_empty:
            raise IndexError("Peek from an empty stack")
        return self.items[-1]
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    def __str__(self):
        return "stack(top -> bottom): " + " -> ".join(map(str, reversed(self.items)))

#Testing    
s = Stack()
s.push(10)
s.push(100)
s.push(150)
print(s)
print(s.pop())
print(s.peek())
print(s.size())
print(s.is_empty())