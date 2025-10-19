# boolean masking 
import numpy as np
arr = np.array([10, 15, 20, 25, 30])    
mask = arr > 20
print("Boolean Mask:", mask)  # Output: [False False False  True  True] 
filtered_arr = arr[mask]    
print("Filtered Array (elements > 20):", filtered_arr)  # Output: [25 30]
# Directly using condition inside indexing
filtered_arr_direct = arr[arr > 20]
print("Filtered Array using direct condition:", filtered_arr_direct)  # Output: [25 30]
# Combining multiple conditions
combined_mask = (arr > 15) & (arr < 30)
filtered_combined = arr[combined_mask]
print("Filtered Array (15 < elements < 30):", filtered_combined)  # Output: [20 25]
# Using np.where for filtering
indices = np.where(arr > 20)
print("Indices of elements > 20:", indices[0])  # Output: [3 4]
filtered_where = arr[indices]
print("Filtered Array using np.where:", filtered_where)  # Output: [25 30]
