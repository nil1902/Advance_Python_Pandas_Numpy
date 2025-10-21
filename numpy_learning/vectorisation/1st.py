list1=[1,2,3,4,5]
list2=[10,20,30,40,50]
result=[x+y for x,y in zip(list1,list2)]
print("Result using loops:", result) 

               
#  vectorisation approach
import numpy as np
arr1=np.array(list1)
arr2=np.array(list2)
result_vec=arr1+arr2  # Vectorised addition
print("Result using vectorisation:", result_vec)

#  vector multiplication with vectorisation
multiplied=result_vec*2  # Vectorised multiplication
print("Multiplied result using vectorisation:", multiplied)


# differenence between broadcasting and vectorisation 
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
vector=np.array([10,20,30])
result_broadcast=matrix+vector  # Broadcasting the vector across each row of the matrix
print("Result using broadcasting:\n", result_broadcast)
#  demonstrating non vectorised approach for matrix addition
result_non_vec=[]
for row in matrix:
    new_row=[]
    for i in range(len(row)):
        new_row.append(row[i]+vector[i])
    result_non_vec.append(new_row)
print("Result using non-vectorised approach:\n", result_non_vec)
#  demonstrating id difference
print("Matrix id:", id(matrix))
print("Vector id:", id(vector))
print("Result id using broadcasting:", id(result_broadcast))
print("Result id using non-vectorised approach:", id(result_non_vec))

#  demonstrating performance difference
import time
# Vectorised approach
start_vec=time.time()
large_arr1=np.random.rand(1000000)
large_arr2=np.random.rand(1000000)
large_result_vec=large_arr1+large_arr2
end_vec=time.time()
print("Time taken for vectorised addition:", end_vec - start_vec)
# Non-vectorised approach
start_non_vec=time.time()
large_list1=large_arr1.tolist()


large_list2=large_arr2.tolist()
large_result_non_vec=[x+y for x,y in zip(large_list1, large_list2)]
end_non_vec=time.time()
print("Time taken for non-vectorised addition:", end_non_vec - start_non_vec)
    