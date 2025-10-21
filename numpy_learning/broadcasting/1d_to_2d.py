import  numpy as np
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
vector=np.array([10,20,30])  # add corresponding elements of each row
result=matrix+vector  # Broadcasting the vector across each row of the matrix

print("Original Matrix:\n", matrix)
print("Vector to be broadcasted:", vector)
print("Result after Broadcasting:\n", result)

# Demonstrating incompatible shapes
incompatible_vector=np.array([1,2])

#  error when shape mismatch ! 
try:
    result_incompatible=matrix+incompatible_vector

except ValueError as e:
    print("Error with incompatible shapes:", str(e))