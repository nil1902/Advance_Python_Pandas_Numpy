# removing element from araay using np.delete(arr, index, axis)
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# remove element at index 1 from flattened array
new_arr1 = np.delete(arr, 1)
print("Array after removing element at index 1 from flattened array:\n", new_arr1)
# remove row at index 0
new_arr2 = np.delete(arr, 0, axis=0)
print("Array after removing row at index 0:\n", new_arr2)
# remove column at index 2
new_arr3 = np.delete(arr, 2, axis=1)
print("Array after removing column at index 2:\n", new_arr3)
# remove multiple elements at index 0 and 2 from flattened array
new_arr4 = np.delete(arr, [0, 2])
print("Array after removing elements at index 0 and 2 from flattened array:\n", new_arr4)
# remove multiple rows at index 0 and 2
new_arr5 = np.delete(arr, [0, 2], axis=0)
print("Array after removing rows at index 0 and 2:\n", new_arr5)
# remove multiple columns at index 0 and 1
new_arr6 = np.delete(arr, [0, 1], axis=1)
print("Array after removing columns at index 0 and 1:\n", new_arr6)
