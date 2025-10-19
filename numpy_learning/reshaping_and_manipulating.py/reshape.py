# arr.reshape(3, 2) => reshape only possible only when dimension is same 
# print("Reshaped Array (3x2):\n", reshaped_arr)
# reshaping does not create copy , return the view only 

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr = arr.reshape(3, 2)
print("Reshaped Array (3x2):\n", reshaped_arr)

#  revel() give me view,  and flatten() give me a copy of array, dont disturn the original array

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
reversed_arr = np.ravel(arr_2d)
flattened_arr = arr_2d.flatten()    
print("Reversed Array using ravel():", reversed_arr)
print("Flattened Array using flatten():", flattened_arr)