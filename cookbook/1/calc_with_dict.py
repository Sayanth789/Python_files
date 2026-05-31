# prices = {

#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 37.20,
#     'FB': 10.75 
# }

# In order to perform useful calculations on the dictionary contents, it is often useful to
# invert the keys and values of the dictionary using zip()

# Here we calculate min and max price and name of stock 

# min_price = min(zip(prices.values(), prices.keys()))

# max_prices = max(zip(prices.values(), prices.keys()))

# print("The minimum price is: ", min_price)
# print("The maximum price is: ", max_prices)

# # To rank the data, use zip() with sorted() 
# prices_sorted = sorted(zip(prices.values(), prices.keys()))
# print("The prices with names: ", prices_sorted)

'''
Finding smallest commnalities in  Two Dictionaries: 
In 2 dict: we find what might have in common.

'''

# a = {

#     'x': 1,
#     'y': 2,
#     'z': 3
# }

# b = {
#    'w': 10,
#    'x': 11,
#    'y': 2 
# }

# # keys are common
# print(a.keys() & b.keys())

# # keys that are not common
# print(a.keys() - b.keys())

# # Find (key,value) pairs in common
# print(a.items() & b.items())

# # dict comprehesion: make a new dict with certain keys removed 

# c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# print("certain items removed ....", c)



# Removing  Duplicates from a Sequence while Maintaining Order 

'''  
You want to eliminate the duplicate values in a sequence, but preserve the order of the
remaining items.

<.> If the values in the sequence are hashable, the problem can be easily solved using a set
and a generator. For example:

'''
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item 
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]            
no_dup = list(dedupe(a))

print(sorted(no_dup))


# For unhashable items in sequence types (dicts) we make a change 
def dedupe_unhash(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x':1, 'y':2},{'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':2}]            
no_dup2 = list(dedupe_unhash(a, key=lambda d: (d['x'], d['y'])))
print(no_dup2)

no_dup2 = list(dedupe_unhash(a, key=lambda d: (d['x'])))

print(no_dup2)