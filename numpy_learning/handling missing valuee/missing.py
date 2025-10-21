## nan mean not a number
# np.isnull(np.array([1, 2, np.nan, 4, np.nan]))  # Check for NaN values
# np.isnan(np.array([1, 2, np.nan, 4, np.nan]))
import numpy as np
data = np.array([1, 2, np.nan, 4, np.nan, 6])
print("Original data:", data)
# Identify missing values
missing_mask = np.isnan(data)   
print("Missing value mask:", missing_mask)


# ||||||||||||||||||||||||||||||||||||||   machine learning dont process nan values  

print(np.nan==np.nan)  # False || interview question, cant compare nan with nan
# Handling missing values by replacing them with the mean of the non-missing values
mean_value = np.nanmean(data)  # Calculate mean ignoring NaNs   
print("Mean value (ignoring NaNs):", mean_value)
data_filled = np.where(missing_mask, mean_value, data)  # Replace NaNs with mean
print("Data after replacing NaNs with mean:", data_filled)


# infinite value handling
data_with_inf = np.array([1, 2, np.inf, 4, -np.inf, 6])
print("Original data with infinities:", data_with_inf)
print(np.isinf(data_with_inf))  # Check for infinite values

# replacing infinite values with large finite numbers
data_no_inf = np.where(np.isinf(data_with_inf), np.finfo(np.float64).max, data_with_inf)
print("Data after replacing infinities:", data_no_inf)
# Summary of functions
# np.isnan(): Identify NaN values
# np.isinf(): Identify infinite values
# np.nanmean(): Compute mean ignoring NaNs
# np.where(): Conditional replacement in arrays
# np.finfo(): Get machine limits for floating point types
# These functions are essential for preprocessing data with missing or infinite values before analysis or modeling.
# Additional example: Removing NaN values from an array


data_with_nans = np.array([1, 2, np.nan, 4, np.nan, 6])
cleaned_data = data_with_nans[~np.isnan(data_with_nans)]  # Remove NaNs
print("Data after removing NaNs:", cleaned_data)
# Additional example: Replacing NaNs with a specific value (e.g., 0)
data_filled_with_zero = np.nan_to_num(data_with_nans, nan=0.0)  # Replace NaNs with 0
print("Data after replacing NaNs with 0:", data_filled_with_zero)

# Additional example: Counting the number of NaNs in an array
num_nans = np.sum(np.isnan(data_with_nans))
print("Number of NaNs in the data:", num_nans)
# Additional example: Replacing infinite values with NaN
data_with_inf_and_nan = np.array([1, 2, np.inf, 4, -np.inf, 6])
data_inf_to_nan = np.where(np.isinf(data_with_inf_and_nan), np.nan, data_with_inf_and_nan)
print("Data after replacing infinities with NaN:", data_inf_to_nan)
# Additional example: Filling NaNs using forward fill method
def forward_fill(arr):
    """Fill NaNs using forward fill method."""
    for i in range(1, len(arr)):
        if np.isnan(arr[i]):
            arr[i] = arr[i - 1]
    return arr
data_ffill = np.array([1, np.nan, np.nan, 4, np.nan, 6])
filled_ffill = forward_fill(data_ffill.copy())
print("Data after forward fill:", filled_ffill)
# Additional example: Filling NaNs using backward fill method
def backward_fill(arr):
    """Fill NaNs using backward fill method."""
    for i in range(len(arr) - 2, -1, -1):
        if np.isnan(arr[i]):
            arr[i] = arr[i + 1]
    return arr
data_bfill = np.array([1, np.nan, np.nan, 4, np.nan, 6])
filled_bfill = backward_fill(data_bfill.copy())

print("Data after backward fill:", filled_bfill)
# Additional example: Interpolating NaN values linearly
def linear_interpolate(arr):

            
    """Interpolate NaNs linearly."""
    n = len(arr)
    for i in range(n):
        if np.isnan(arr[i]):
            # Find previous and next non-NaN values
            prev_index = i - 1
            next_index = i + 1
            while prev_index >= 0 and np.isnan(arr[prev_index]):
                prev_index -= 1
            while next_index < n and np.isnan(arr[next_index]):
                next_index += 1
            if prev_index >= 0 and next_index < n:
                arr[i] = (arr[prev_index] + arr[next_index]) / 2
            elif prev_index >= 0:
                arr[i] = arr[prev_index]
            elif next_index < n:
                arr[i] = arr[next_index]
    return arr
data_interp = np.array([1, np.nan, np.nan, 4, np.nan, 6])
filled_interp = linear_interpolate(data_interp.copy())
print("Data after linear interpolation:", filled_interp)
print("Data after backward fill:", filled_bfill)
print("Data after linear interpolation:", filled_interp)