import numpy as np
arr = np.array([1, 2,  5, 6])
print("Array Dimensions:", arr[2])  # Output: 2
subset = arr[1:4]
print("Subset of Array:", subset)  # Output: [2 5 6]
arr[2] = 10
print("Modified Array:", arr)  # Output: [ 1  2 10  6]
# -ve indexing also present in python  , so ow can i make the negative indexing in numpy
arr_neg = np.array([10, 20, 30, 40, 50])
print("Element at -1 index:", arr_neg[-1])  # Output: 50
print("Elements from -4 to -1:", arr_neg[-4:-1])  # Output: [20 30 40]
arr_neg[-2] = 100
print("Modified Array with -ve indexing:", arr_neg)  # Output: [ 10  20 100  40  50]