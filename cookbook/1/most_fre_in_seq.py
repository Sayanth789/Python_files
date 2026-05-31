# Determining the most frequent items in a sequence.

'''  We use Collections.Counter 
It even comes with
a handy most_common() method that will give you the answer.
'''
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
#     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
#     'my', 'eyes', "you're", 'under'
# ]

# from collections import Counter
# word_counts = Counter(words)

# top_three = word_counts.most_common(1)
# print(top_three)


# sorting LIst of Dictionaries by a common key 
''' 
You have a list of dictionaries and you would like to sort the entries according to one
or more of the dictionary values.
'''

# Sorting this type of structure is easy using the operator module’s itemgetter function.

# rows = [
#     {'fname':'Brian', 'lname': 'Jonnes', 'uid': 1002},
#     {'fname':'David', 'lname': 'Bezely', 'uid': 1003},
#     {'fname':'John', 'lname': 'Clerk', 'uid': 1001},
#     {'fname':'Indiana', 'lname': 'Jonnes', 'uid': 1005},

# ]

# It’s fairly easy to output these rows ordered by any of the fields common to all of the
# dictionaries. For example:

# from operator import itemgetter

# rows_by_fname = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))

# print(rows_by_fname)
# print(rows_by_uid)

# Itemgetter can accept multiple keys.

# rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))

# print(rows_by_lfname)


# Grouping Records Together Based on a Field 
''' 
You have a sequence of dictionaries or instances and you want to iterate over the data
in groups based on the value of a particular field, such as date.
'''

# rows = [

#     {'address': '5412 N CLARK', 'date': '07/01/2012'},
#     {'address': '5148 N CLARK', 'date': '07/04/2012'},
#     {'address': '5800 E 58TH', 'date': '07/02/2012'},
#     {'address': '2122 N CLARK', 'date': '07/03/2012'},
#     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]


# from operator import itemgetter 
# from itertools import groupby 


# rows.sort(key=itemgetter('date'))

# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print('      ', i)



''' Filtering seqeuence :
Inside a seq: need to extract values or reduce seq: using
some criteria
'''
# mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# greater = [n for n in mylist if n > 0]
# lesser = [n for n in mylist if n <  0]

# print(greater)
# print(lesser)

# import math 

# print([math.sqrt(n) for n in mylist if n > 0])

# # clipping 
# clip_neg = [n if n > 0 else 0 for n in mylist]
# print(clip_neg)

# clip_pos = [n if n < 0 else 0 for n in mylist]
# print(clip_pos)



''' Mapping Names to Sequence Elements 

You have code that accesses list or tuple elements by position, but this makes the code
somewhat difficult to read at times. You’d also like to be less dependent on position in
the structure, by accessing the elements by name

* collections.namedtuple() provides these benefits, while adding minimal overhead
over using a normal tuple object. collections.namedtuple() is actually a factory
method that returns a subclass of the standard Python tuple type. You feed it a type
name, and the fields it should have, and it returns a class that you can instantiate, passing
in values for the fields you’ve defined, and so on.

'''

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)

print(len(sub))