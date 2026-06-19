import collections 

def _upper(key):
    try:
        return key.upper()
    except AttributeError:
        return key
    
class UpperCaseMixin:
    def __setitem__(self, key, item):
        super().__setitem__(_upper(key), item)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))        

class UpperDict(UpperCaseMixin, collections.UserDict):
    pass 
class UpperCounter(UpperCaseMixin, collections.Counter):
    """ Specified 'counter' uppercase string keys """


''' 
UpperDict behaves like a case-insensisitive mapping


'''
d = UpperDict([('a', 'letter A'), (2, 'digit two')])
print(list(d.keys()))

d['b'] = 'letter B'
print('b' in d)

print(d['a'], d.get('B'))

print(list(d.keys()))

c = UpperCounter('BaNaNa')
print(c.most_common)
