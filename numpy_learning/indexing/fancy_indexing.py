import numpy as np
arr = np.array([1, 2, 3,4, 5, 6])
print("Accessing element at row 0, column 1:", arr[[0, 1]])  # Output: 2 # select multiple elements
print("Accessing elements at rows [0,1] and columns [1,2]:", arr[3])  # Output: [2 6]