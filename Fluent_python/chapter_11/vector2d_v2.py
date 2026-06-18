from array import array
import math 


class Vector2d:
    typecode = 'd'


    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


    def __iter__(self):
        return (i for i in (self.x, self.y))
    

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self))
                )
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    

    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
        
   
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)    

v1 = Vector2d(3,4)
print(v1.x, v1.y) 

x, y = v1 
print(x, y)
print(v1)

octets = bytes(v1)
print(octets)
print(abs(v1))


# Tests of `format()` with cartesian coordinates 
print(format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))

# Tests of angle method 
print(Vector2d(0, 0).angle())
print( Vector2d(1, 0).angle())
epsilon = 10**-8
print(abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon)
print( abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon)

# Tests of ``format()`` with polar coordinates:
print(format(Vector2d(1, 1), 'p'))
print( format(Vector2d(1, 1), '.3ep'))
print(format(Vector2d(1, 1), '0.5fp'))