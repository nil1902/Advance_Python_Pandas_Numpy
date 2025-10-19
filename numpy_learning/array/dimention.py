# ndimension of array 
import numpy as np
arr = np.array([1, 2, 3])
arr_2d= np.array([[1,2,3],[4,5,6]])
arr_3d= np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Array Dimensions:", arr.ndim)  # Output: 2
print("2D Array Dimensions:", arr_2d.ndim)  # Output: 2
print("3D Array Dimensions:", arr_3d.ndim)  # Output: 3 