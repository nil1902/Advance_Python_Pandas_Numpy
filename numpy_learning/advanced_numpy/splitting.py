# splitting using np.split() vsplit() and hsplit()
import numpy as np

try:
    # Create a 3x4 array
    arr = np.array([[1, 2, 3, 4], 
                    [5, 6, 7, 8], 
                    [9, 10, 11, 12]])
    print(f"Original Array Shape: {arr.shape}")
    print("Original Array:\n", arr, "\n")

    # Split into 2 sub-arrays along rows (axis=0)
    split_arr = np.split(arr, 3, axis=0)  # Changed to 3 for even splitting
    print("Split Array along rows (axis=0):")
    for i, sub_arr in enumerate(split_arr):
        print(f"Sub-array {i}:\n", sub_arr)
    print()

    # Horizontal split into 2 sub-arrays
    hsplit_arr = np.hsplit(arr, 2)  # Split into 2 parts horizontally
    print("Horizontal Split (along columns):")
    for i, sub_arr in enumerate(hsplit_arr):
        print(f"Sub-array {i}:\n", sub_arr)
    print()

    # Vertical split requires array with even divisions
    if arr.shape[0] % 3 == 0:  # Check if array can be split evenly
        vsplit_arr = np.vsplit(arr, 3)
        print("Vertical Split (along rows):")
        for i, sub_arr in enumerate(vsplit_arr):
            print(f"Sub-array {i}:\n", sub_arr)

except ValueError as e:
    print(f"Error in splitting: {str(e)}")
    print("Make sure the array can be split evenly")
except Exception as e:
    print(f"Unexpected error: {str(e)}")
