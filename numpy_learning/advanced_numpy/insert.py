# np.insert(arr, 2, 99)  # Insert 99 at index 2
# print("Array after insertion:", new_arr)  # Output: [ 1  2 99  3  4  5  6]
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.insert(arr, 2, 99)  # Insert 99 at index 2
print("Array after insertion:", new_arr)  # Output: [ 1  2 99  3  4  5  6]  
# Inserting multiple values
new_arr_multi = np.insert(arr, [1, 3, 5], [100, 200, 300])
print("Array after multiple insertions:", new_arr_multi)  # Output: [  1 100  2 200  3 300  4  5  6]
# Inserting values in a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
new_arr_2d = np.insert(arr_2d, 1, [99, 100, 101], axis=0)  # Insert a new row at index 1
print("2D Array after row insertion:\n", new_arr_2d)
new_arr_2d_col = np.insert(arr_2d, 2, [77, 88], axis=1)  # Insert a new column at index 2
print("2D Array after column insertion:\n", new_arr_2d_col)
# Inserting values at the end
new_arr_end = np.insert(arr, arr.size, 999)
print("Array after inserting at the end:", new_arr_end)  # Output: [  1   2   3   4   5   6 999]
# Inserting values at the beginning
new_arr_begin = np.insert(arr, 0, -1)
print("Array after inserting at the beginning:", new_arr_begin)  # Output: [-1  1  2  3  4  5  6]
# Note: np.insert does not modify the original array; it returns a new array with the inserted values.
# You can specify the axis parameter to insert along rows (axis=0) or columns (axis=1) in multi-dimensional arrays.
# You can also insert multiple values at multiple indices by providing lists for both indices and values.
# Be cautious when inserting values in multi-dimensional arrays, as the shape of the inserted values must match the shape of the array along the specified axis.
# The function can be used to insert values at specific positions, at the beginning, or at the end of the array.
# The original array remains unchanged after the insertion operation.
# np.insert(arr, 2, 99)  # Insert 99 at index 2
# print("Array after insertion:", new_arr)  # Output: [ 1  2 99  3  4  5  6]



# append
new_arr = np.append(arr, 99)  # Append 99 at the end
print("Array after appending:", new_arr)  # Output: [ 1  2  3  4  5  6 99]
# Inserting multiple values   
new_arr_multi = np.append(arr, [100, 200, 300])
print("Array after multiple appends:", new_arr_multi)  # Output: [  1   2   3   4   5   6 100 200 300]
# Inserting values in a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
new_arr_2d = np.append(arr_2d, [[7, 8, 9]], axis=0)  # Append a new row
print("2D Array after row append:\n", new_arr_2d)
new_arr_2d_col = np.append(arr_2d, [[10], [11]], axis=1)  # Append a new column
print("2D Array after column append:\n", new_arr_2d_col)
# # Note: np.append does not modify the original array; it returns a new array with the appended values.

#  concatenate
arr1 = np.array([1, 2, 3])  
arr2 = np.array([4, 5, 6])
new_arr = np.concatenate((arr1, arr2))  # Concatenate arr1 and arr2
print("Array after concatenation:", new_arr)  # Output: [1 2 3 4 5 6]
# Concatenating multiple arrays
arr3 = np.array([7, 8, 9])
new_arr_multi = np.concatenate((arr1, arr2, arr3))
print("Array after multiple concatenations:", new_arr_multi)  # Output: [1 2 3 4 5 6 7 8 9]
# Concatenating 2D arrays
arr_2d_1 = np.array([[1, 2], [3, 4]])
arr_2d_2 = np.array([[5, 6], [7, 8]])
new_arr_2d = np.concatenate((arr_2d_1, arr_2d_2), axis=0)  # Concatenate along rows
print("2D Array after row concatenation:\n", new_arr_2d)
new_arr_2d_col = np.concatenate((arr_2d_1, arr_2d_2), axis=1)  # Concatenate along columns
print("2D Array after column concatenation:\n", new_arr_2d_col)
# Note: np.concatenate requires the arrays to have compatible shapes along the specified axis.
