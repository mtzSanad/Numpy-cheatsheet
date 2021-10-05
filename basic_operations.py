import numpy as np
from numpy.core.fromnumeric import ndim

# ndarray numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
a = np.array([1, 2, 3])
print(a)

a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a2)

a3 = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a3)

a4 = np.array([1, 2, 3, 4, 5], dtype=complex)
print(a4)

# numpy data types | numpy.dtype(object, align, copy) | https://www.tutorialspoint.com/numpy/numpy_data_types.htm
dt = np.dtype(np.int32)
print(dt)
print(a4.dtype)

# Array attributes
print(a2.shape)
a2.shape = (3, 2)
print(a2)
a2.shape = (2, 3)
b = a2.reshape(3, 2)
print(b)

c = np.arange(24)
print(c)
print(c.ndim)
x = c.reshape(2, 4, 3)
print(x)

print(x.itemsize)  # length of each element of array in bytes
print(x.flags)

# Array creation
