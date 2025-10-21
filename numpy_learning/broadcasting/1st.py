price = [10, 20, 30, 40, 50]
import numpy as np
arr = np.array(price)
new_arr = arr + 5  # Vectorised operation to add 5 to each element
print("Original array:", arr)
print("New array after adding 5:", new_arr)
print("Original array id:", id(arr))
print("New array id:", id(new_arr))

discount=10
final_price=[]
for p in price:
    final_price.append(p - discount)    
print("Final price after discount using loop:", final_price)
final_price_vec = arr - discount
print("Final price after discount using vectorisation:", final_price_vec)
print("Final price array id:", id(final_price_vec))
