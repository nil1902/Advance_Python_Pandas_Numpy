# stack the array using vstack, hstack, dstack
import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
# Vertical stacking
vstacked = np.vstack((arr1, arr2))
print("Vertically Stacked Array:\n", vstacked)
# Horizontal stacking
hstacked = np.hstack((arr1, arr2))
print("Horizontally Stacked Array:\n", hstacked)
# Depth stacking
dstacked = np.dstack((arr1, arr2))
print("Depth Stacked Array:\n", dstacked)
