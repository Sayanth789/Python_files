'''
Iteration is one of Python’s strongest features. At a high level, you might simply view
iteration as a way to process items in a sequence. However, there is so much more that
is possible, such as creating your own iterator objects, applying useful iteration patterns
in the itertools module, making generator functions, and so forth.

 You need to process items in an iterable, but for whatever reason, you can’t or don’t want
to use a for loop.
To manually consume  an iterable, we use next() function and write code to catch the StopIteration exception


'''

# with open('./test.txt') as f:
#     try:
#         while True:
#             line = next(f)
#             print(line, end="")
#     except StopIteration:
        # pass 


''' Delegating Itertion
You have built a custom container object that internally holds a list, tuple, or some other
iterable. You would like to make iteration work with your new container.


Typically, all you need to do is define an __iter__() method that delegates iteration to
the internally held container. For example:
'''

# class Node:
#     def __init__(self, value):
#         self._value = value 
#         self._children = []

#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
    
#     def  add_child(self, node):
#         self._children.append(node)

#     def __iter__(self):
#         return iter(self._children)


# if __name__ == "__main__":
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)

#     for ch in root:
#         print(ch)



# Creating new Interation Patterns with Generators 
'''  
You want to implement a custom iteration pattern that’s different than the usual built-
in functions (e.g., range(), reversed(), etc.).

f you want to implement a new kind of iteration pattern, define it using a generator
function.

Here’s a generator that produces a range of floating-point numbers:
'''

def frange(start, stop, increment):
    x = start 
    while x < stop:
        yield x 
        x += increment

# To use such a function, you iterate over it using a for loop or use it with some other
# function that consumes an iterable (e.g., sum(), list(), etc.). For example:

with open('loop.txt', 'w') as f:
        for n in frange(0, 4, 0.5):

            f.write(f"Line numbr: {n}\n")
        

# The mere presence of a yield statement turn a fun: to a generator 
# Unlike a normal function, a generator only runs in response to iteration


''' 
Implementing the Itertator Protocol 

You are building custom objects on which you would like to support iteration, but would
like an easy way to implement the iterator protocol.

By far, the easiest way to implement iteration on an object is to use a generator function.

To implement an iterator that traverse nodes in a deptj-first pattern
Here is how we do it

'''

class Node:
     def __init__(self, value):
          self._value = value 
          self._children = [] 

     def __repr__(self):
          return  'Node({!r})'.format(self._value)

     def add_child(self, node):
          self._children.append(node)

     def  __iter__(self):
          return iter(self._children)

     def depth_first(self):
          yield self 
          for c in self:
               yield from c.depth_first()

# Example
if __name__ == '__main__':
        root = Node(0)
        child1 = Node(1)
        child2 = Node(2)
        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(Node(3))
        child1.add_child(Node(4))
        child2.add_child(Node(5))  

        for ch in root.depth_first():
             print(ch)                     
        # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
        #        

''' 
Iterting in Reverse :

To iterate in reverse over a sequence 

Use builtin reversed() funtion 

Reversed iteration only works if the object in question has a size that can be determined
or if the object implements a __reversed__() special method. If neither of these can
be satisfied, you’ll have to convert the object into a list first. For example:
        # Print a file backwards
        f = open('somefile')
        for line in reversed(list(f)):
        print(line, end='')

'''        

'''  
Defining Generator Function with Extra State 

<> 
You would like to define a generator function, but it involves extra state that you would
like to expose to the user somehow.

<> If you want a generator to expose extra state to the user, don’t forget that you can easily
implement it as a class, putting the generator function code in the __iter__() method.
For example:

# '''

# from collections import deque 

# class linehistory:
#      def __init__(self, lines, histlen=3):
#           self.lines = lines
#           self.history = deque(maxlen=histlen)

#      def __iter__(self):
#           for lineno, line in enumerate(self.lines, 1):
#                self.history.append(lineno, line)
#                yield line 

#      def clear(self):
#           self.history.clear()

# with open('somefile.txt') as f:
#      lines = linehistory(f)
#      for line in lines:
#           if 'python' in line:
#                for lineno, hline in lines.history:
#                     print('{}:{}'.format(lineno, hline), end="")


'''  
Taking a Slice of an Iterator 

You want to take a slice of data produced by an iterator, but the normal slicing operator
doesn’t work.

The itertools.islice() function is perfectly suited for taking slices of iterators and
generators. For example:

import itertools 
for x in itertools.islice(c, 10, 20):
    print(x)

'''

'''  
Skipping first part of an Iterable 

You want to iterate over items in an iterable, but the first few items aren’t of interest and
you just want to discard them.


from itertools import dropwhile 

with open('/etc/passwd') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
                print(line, end='')

# Iterating over All Possible Combo or Permutations 
<>
items = ['a', 'b', 'c']
from itertools import permutations 

for p in permutations(items):
    print(p)

    
for p in permutations(items, 2):
        print(p)    

        # This is for permutation of small length 
<>


'''


# Iterting OVer Multiple Sequence Simultaneously
# 
# To iterate over the items contained in more than one sequence at a time

''' 
To iterate over more than one sequence simultaneously, use the zip() function. For eg:

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y i zip(xpts, ypts):
    print(x, y)
---------------------------------------------------------

Flattening a Nested Sequence :

To flattern a nested seq: into a single list of values.

<> This can be easily solved using recursive generator  involving a yield
from statement 

from collections import Iterable 

def flatten(items, ignore_tpyes=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from Flatten(x)
        else:
            yield x 
items = [1, 2, [3, 4, [5, 6], 7], 8]

for x in flatten(items):
    print(x)


'''

