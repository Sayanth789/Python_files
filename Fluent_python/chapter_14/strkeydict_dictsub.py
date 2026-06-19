
class StrKeyDict(dict):

    def __init__(self, iterable=None, **kwds):
        super().__init__()
        self.update(iterable, **kwds)

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

    def __setitem__(self, key, item):
        super().__setitem__(str(key), item)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def update(self, iterable=None, **kwds):
        if iterable is not None:
            try:  # duck typing FTW!
                pairs = iterable.items()
            except AttributeError:
                pairs = iterable
            for key, value in pairs:
                self[key] = value
        if kwds:
            self.update(kwds)

"""
StrkeyDict always converts non-strng keys to 'str'

This is a varaiton of `strkeydict.StrKeyDict` implemented 
as a `dict` build-in subclass (instead of a `UseDict` subclass)

"""

d = StrKeyDict([(2, 'two'), ('4', 'four')])
print(sorted(d.keys()))
print(d['2'])
print(d['4'])

# Tests for item retrieval using `d.get(key)` notation::
print(d.get('2'))
print(d.get('4'))
print(d.get(1, 'N/A'))

print(2 in d)
print(1 in d)
d[0] = 'zero'
print(d['0'])


# Tests for update using a `dict` or a sequence of pairs::
d.update({6:"six", "8":"eight"})
print(sorted(d.keys()))

d.update([(10, 'ten'), ('12', 'twelve')])
print(d.keys())
print(d.update([1, 3, 5]))
