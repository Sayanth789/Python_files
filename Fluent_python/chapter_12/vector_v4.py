from array import array 
import reprlib 
import math 
import functools 
import operator 



class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.finc('['):-1]
        return f"Vector({components})"
    
    def __str__(self):
        return str(tuple(*self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(self._components)
                )
    
    def __eq__(self, other):
        return (len(self) == len(other) and 
                all(a == b) for a, b in zip(self, other))
    
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
    __match_arg__ = ('x', 'y', 'z', 't') 

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_arg__.index(name)
        except ValueError:
            pos = -1 
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0]) 
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)   
    
'''
This method is designed for extreme performance.

If you had a vector with 1,000,000 numbers, converting those raw bytes back into a standard Python list would require Python to create 1,000,000 separate float objects in memory, which is slow and heavy.

By using memoryview and .cast(), Python essentially just points a camera at the existing binary data, re-interprets it instantly, and passes it straight into the new array. It is computationally nearly instantaneous.
'''    

# Test for hashing 
v1 = Vector([3, 5])
v2 = Vector([3.1, 5.2])
v3 = Vector([3, 4, 5])
v5 = Vector(range(6))
print(hash(v1), hash(v3), hash(v5))

# Most hash codes of non-integers vary from a 32-bit to 64-bit CPython build::

import sys 
hash(v2) == (384307168202284039 if sys.maxsize > 2**32 else 357915986)

hash = hash(v2)

def print_hash(current_hash):
    h1 = 384307168202284039
    h2 = 357915986
    if current_hash == h1:
        print(f"It matches the 64-bit hash: {h1}")
    elif current_hash == h2:
        print(f"It matches the 32-bit hash: {h2}")
    else:
        print(f"It is a different hash: {current_hash}")

print_hash(hash)
