'''  
Implementing visitor pattern without Recursion 
<>
You’re writing code that navigates through a deeply nested tree structure using the visitor
pattern, but it blows up due to exceeding the recursion limit. You’d like to eliminate the
recursion, but keep the programming style of the visitor pattern.


<>
Clever use of generators can sometimes be used to eliminate recursion from algorithms
involving tree traversal or searching
'''

import types 

class Node:
    pass 


class NodeVisitor:
    def visit(self, node):
        stack = [ node ]
        last_result = None 
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None 
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop())) 
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result
    
    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth =  getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit 
        return meth(node)
    
    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


'''  
Managing memory in Cyclic Data structures
<>
Your program creates data structures with cycles (e.g., trees, graphs, observer patterns,
etc.), but you are experiencing problems with memory management

<>
A simple example of a cyclic data structure is a tree structure where a parent points to
its children and the children point back to their parent. For code like this, you should
consider making one of the links a weak reference using the weakref library. For
example:

'''
    
import weakref 

class Node:
    def __init__(self, value):
        self.value = value 
        self._parent = None 
        self.children = [] 


    def __repr__(self):
        return 'Mode({!r:})'.format(self.value)

    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter 
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


# The implementation allow the parent to quitely die . For eg:
root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)
del root 
print(c1.parent)
