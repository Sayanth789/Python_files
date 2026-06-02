''' 
To perform matrix and linear algebra operations, such as matrix multiplication,
finding determinants, solving linear equations, and so on.

'''

import numpy as np 
m = np.matrix([[1,-2,3], [0,4,5], [7,8,-9]])

print(m)

# Transpose 
print(m.T)

# Inverse 
print(m.I)

# Create a vector and multiply
v = np.matrix([[2], [3], [4]])

print(v)

''' For more operations we use linalg subpackage '''
import numpy.linalg 

# Determinant 
deter = numpy.linalg.det(m)

print(deter)

'''   
I must explore more lin lagebra

'''