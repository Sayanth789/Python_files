'''  
Working with binary, Octal , and Hexadecimal Integers

To Convert or output integer represented by binary,  octal or hexadecimal

we use bin(), oct() and hex() respectively. 
'''
# x = 1234
# print(bin(x))

# print(oct(x))


# print(hex(x))


# Or can use format() so 0b, 0o, or 0x  prefixes vanish 

# print(format(x, 'b'))

# print(format(x, 'o'))


# print(format(x, 'x'))


'''  
Integers are signed, so if we are working with negative numbers, the output will also
include a sign. For example:
'''

# x = -1234 
# print(format(x, 'b'))

'''  
If we need to produce an unsigned value instead, we’ll need to add in the maximum
value to set the bit length
'''
# x = -1234

# print(format(2**32 + x, 'b'))
# print(format(2**32 + x, 'x'))
# print(format(2**32 + x, 'o'))


''''   
----------------

Packing and Unpacking Large Integers from Bytes

You have a byte string and you need to unpack it into an integer value. Alternatively,
you need to convert a large integer back into a byte string.

----------------
'''

# Suppose the progran needs to work with a 16-element byte string that 
# holds a 128 bit integer value. Eg:

# data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

# To interpret bytes as an integer , use int.from_bytes() and specify byte 
# ordering as this 

# print(len(data))

# print(int.from_bytes(data, 'little'))
# print(int.from_bytes(data, 'big'))

# To convert large int value back to byte string we use int.to_butes() 
# x = 94522842520747284487117727783387188
# print(x.to_bytes(16, 'big'))
# print(x.to_bytes(16, 'little'))

'''   
:+:  Complex math :+:

'''

# import numpy as np 
# a = np.array([2+3j, 4+5j, 6-7j, 8+9j])

# print(a)
# print(a + 2)

# print(np.sin(a))


'''  Working with Infinity and NaNs '''

# a = float('inf')
# b = float('-inf')
# c = float('nan')
# print(a)

# print(b)
# print(c)

# import math 
# print(math.isinf(a))
# print(math.isnan(a))

''''  
Calculating with Fractions

'''

# from fractions import Fraction 
# a = Fraction(5, 4)
# b = Fraction(7, 16)

# print(a + b)

# print(a * b)

# c = a * b
# print(c.numerator)

# print(c.denominator)


# print(float(c))

# print(c.limit_denominator(8))

# # Convert a float to fraction 
# x = 3.75 
# y = Fraction(*x.as_integer_ratio())
# print(y)

'''  Calculating with large Numerical Arrays 
You need to perform calculations on large numerical datasets, such as arrays or grids.
'''

import numpy as np 

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(x * 2)
print(x + 10)


# These are numpy arrays 
ax = np.array([1,2,3,4])
ay = np.array([5, 6, 7, 8])

print(ax * 2)

print(ax + 10)

print(ax + ay)


def f(x):
    return 3*x**2 - 2*x + 7

print(f(ax))


'''  
to make a two-dimensional grid of 10,000 by 10,000 floats :

'''

grid = np.zeros(shape=(1000, 1000), dtype=float)

print(grid)
grid += 10
print(grid)

print(np.sin(grid))