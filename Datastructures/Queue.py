# this is the Queue datastructure:
class Queue:
    def __init__(self):
        self.items = []
    def enque(self, item):
        """Adding elements to the queue."""
        self.items.append(item)
    def deque(self):
        """Remove an element if the queue is empty, raise an index error."""        
        if is_empty(self):
            raise IndexError("Deque an empty queue")
        return self.items.pop(0)
    def front(self):
        "Return the front without removing it. Raise an indexerror if queue is empty."
        if self.is_empty():
            raise IndexError("Front from an empty queue.")
        return self.items[0]
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the size of the queue"""
        return len(self.items)
    
    def __str__(self):
        return "Queue(front -> rear): " + " -> ".join(map(str, self.items))

q = Queue()
q.enque("A")
q.enque("B")
q.enque("C")
print(q)
print(q.deque())
print(q.front())
print(q.size())
print(q.is_empty())