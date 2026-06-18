from array import array 
import reprlib
import math 

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)


    def __repr__(self):
        components = reprlib.repr(self._components)
        componets = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(self._components))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(*self)
    
    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

print(Vector([3.1, 4.2]))
print(Vector((3, 4, 5)))

print(Vector(range(10)))

# Tests with 2-dimensions (same results as ``vector2d_v1.py``)::
v1 = Vector([3, 4])
x, y = v1 

print(x, y)
print(v1)
octets = bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1), bool(Vector([0, 0])))

# Test of ``.frombytes()`` class method:
v1_clone = Vector.frombytes(bytes(v1))
print(v1_clone)
print(v1 == v1_clone)

# Tests with 3-dimensions::
v1 = Vector([3, 4, 5])
x, y, z = v1 
print(x, y, z)
print(v1)

v1_clone = eval(repr(v1))
print(int(v1 == v1_clone))

# Tests with many dimensions::
v7 = Vector(range(7))
print(v7)

print(abs(v7))

# Test of ``.__bytes__`` and ``.frombytes()`` methods::
v1 = Vector([3, 4, 5])
v1_clone = Vector.frombytes(bytes(v1))
print(v1_clone)

print(v1 == v1_clone)
