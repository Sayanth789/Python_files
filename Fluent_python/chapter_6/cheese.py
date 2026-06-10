class Cheese:

    def __init__(self, kind):
        self.kind = kind 

    def __repr__(self):
        return f'Cheese({self.kind!r})'    

c = Cheese("cheddar")
print(isinstance(c, Cheese))
print(c.__class__)


import weakref 
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'),Cheese('Tilsit'), Cheese('Brie'), Cheese('Paremsan')]


for cheese in catalog:
    stock[cheese.kind] = cheese 

print(sorted(stock.keys()))

del catalog
print(sorted(stock.keys()))

del cheese 
# print(sorted(sorted.keys()))
