import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array Dimensions:", arr.dtype)  # Output: 2

# change the datatype using astype() function
arr_float = arr.astype(float)
print("Array with float datatype:", arr_float)
arr_str = arr.astype(str)
print("Array with string datatype:", arr_str)