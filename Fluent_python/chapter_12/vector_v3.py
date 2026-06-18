from array import array 
import reprlib 
import math
import operator

'''
In this context, typecode is a class attribute that defines the specific C-level data type that the vector's underlying array will store.
'''
class Vector:
    typecode = 'd'  # to tell python, this vector only stores double-precision floating point numbers.

    def __init__(self, compoents):
        self._components = array(self.typecode, compoents)

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
                bytes(self._components)
                )
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
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

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
            
        super().__setattr__(name, value)
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv =  memoryview(octets[1:].cast(typecode))
        return cls(memv)
    

# Attribytes setting 
v1= Vector(range(7))
v1.X = 'albatros'

print(v1.X)
v1.ni = 'Ni!'
print(v1.ni)



    
