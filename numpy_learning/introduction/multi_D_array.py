import numpy as np
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D Array (Matrix):")
print(matrix)

# creating array from python lists 

print(np.zeros((3,4)))  # 3 rows and 4 columns of zeros
print(np.ones((2,5))  ) # 2 rows and 5 columns of ones with shape(rows,columns)
print(np.full((3,3), 7)) # 3x3 array filled with 7s
print(np.eye(4)  )      # 4x4 Identity matrix

# creating sequence number in array
# arrange() function
# arrange(start, stop, step)
print(np.arange(10))        # numbers from 0 to 9
print(np.arange(5,15))     # numbers from 5 to 14
print(np.arange(0,20,2))   # even numbers from 0 to 18
print(np.arange(1,10,3))   # numbers from 1 to 9