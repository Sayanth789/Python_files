# To make a list of largest or smallest N items in a collection 

# We use heapq module

# import heapq

# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 74, 2]

# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))


# portfolio = [
#     {'name': 'IDM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.21},
#     {'name': 'FB', 'shares': 200, 'price': 21.1},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}    
    
# ]

# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])

# print(f"Cheap {cheap}")
# print(f"expensive {expensive}")

# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# heap = list(nums)
# heapq.heapify(heap)
# the heap[0] is always smallest item. 


# print(heap)


'''
We want to implement a queue that sorts items by a given priority and always returns the 
item with highest priority on each pop opeartion
'''
# The below class implement heapq module using simple pq.

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0 

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1    
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]    

class Item:
    def __init__(self, name):
        self.name = name 
    def _repr__(self):
        return 'Item{!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

p = q.pop()
print(p)

''' 
Defaultdict:



d = {}
for key, value in pairs:
    if key not in d:
        d[key] = [] 
        d[key].append(value)

using defaultdict make it simpler and cleaner 

d = defauldict(list)
for key, value in pairs:
    d[key].append(value)
'''

# To control insertion or serialization of a dict we use OrderedDict 

from collections import OrderedDict 
d = OrderedDict() 

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

''' OrderedDict maintains a dll that orders the keys according to insertion order
When a new item is first inserted, it is placed at the end of this list.

But it consume more than 2x as normal dict space
'''    
