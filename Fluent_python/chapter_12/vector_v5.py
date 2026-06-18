from array import array 
import reprlib
import math 
import functools 
import operator 
import itertools


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))
    

    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.hypot(*self)
    
    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]

    __match_args__ = ('x', 'y', 'z', 't')

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    def angle(self, n):
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2  - a 
        else:
            return a
        
    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))
    
    def __format__(self, format_spec):
        if format_spec.endswith('h'): # hyperspherical coordinate 
            format_spec = format_spec[:-1]
            coords = itertools.chain([abs(self)],
                                     self.angles()
                                     )
            outer_format = '<{}>'
        else:
            coords = self 
            outer_format = '({})'

        components = (format(c, format_spec) for c in coords)
        return outer_format.format(', '.join(components))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    
# Testing hashing 
v1 = Vector([3, 4])
print(v1)    

v2 = Vector([3.1, 4.2]) 
print(v2)

v3 = Vector([3, 4, 5])
print(v3)

# Tests of ``format()`` with Cartesian coordinates in 2D::

v1 = Vector([3, 4])
print(format(v1))

print(format(v1, '.2f'))

print(format(v1, '.3e'))

# Tests of ``format()`` with Cartesian coordinates in 3D and 7D::
v7 = format(Vector(range(7)))
print(v7)

# Test for ``format()`` with shperical coordinates in 2D, 3D, and 4D::

print(format(Vector([1, 1]), 'h'))

print(format(Vector([1, 1]), '.3eh'))
print(format(Vector([1, 1]), '0.5fh'))
print( format(Vector([2, 2, 2]), '.3eh'))
print(format(Vector([0, 0, 0]), '0.5fh'))
print( format(Vector([2, 2, 2, 2]), '.3eh'))
print(format(Vector([0, 1, 0, 0]), '0.5fh'))
