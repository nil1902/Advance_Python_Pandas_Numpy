# splitting using np.split() vsplit() and hsplit()
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Split into 2 sub-arrays along rows
split_arr = np.split(arr, 2, axis=0)
print("Split Array along rows:\n", split_arr)
# Vertical split into 2 sub-arrays
vsplit_arr = np.vsplit(arr, 2)
print("Vertically Split Array:\n", vsplit_arr)
# Horizontal split into 2 sub-arrays
hsplit_arr = np.hsplit(arr, 2)
print("Horizontally Split Array:\n", hsplit_arr)
