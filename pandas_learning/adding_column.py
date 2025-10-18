# # i can add new column in my data set by 2 ways 
# 1. using square brackets
# 2. using insert() method

import pandas as pd
data={
    'Name':['Alice','Bob','Charlie','David'], 
    'Age':[24,27,22,32],
    'City':['New York','Los Angeles','Chicago','Houston'],
    'salary':[70000,80000,60000,90000],
    'performance_score':[88,92,85,95]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# 1. Adding column using square brackets
df['Experience'] = [2, 3, 1, 5]  #
Bonus=df['salary'] *0.1
df['Bonus']=Bonus

print("\nDataFrame after adding 'Experience' column using square brackets:")
print(df)

# 2. Adding column using insert() method
df.insert(2, 'Department', ['HR', 'Finance', 'IT', 'Marketing'])  # inserting at index 2  || df.insert(loc, "column", value)
print("\nDataFrame after adding 'Department' column using insert() method:")
print(df)

id=['E001','E002','E003','E004']
df.insert(0,'Employee_ID',id)
print("\nDataFrame after adding 'Employee_ID' column at the beginning:")
print(df)