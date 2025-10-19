import pandas as pd 
# pd.merge(df1,df2, how='inner', on='key_column')  # inner join
# pd.merge(df1,df2, how='outer', on='key_column')  # outer join
# pd.merge(df1,df2, how='left', on='key_column')   # left join
# pd.merge(df1,df2, how='right', on='key_column')  # right join
# Example of merging two DataFrames
data1 = {
    'EmployeeID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
}
data2 = {
    'EmployeeID': [3, 4, 5, 6],
    'Department': ['HR', 'IT', 'Finance', 'Marketing']
}
df1 = pd.DataFrame(data1)
df2=pd.DataFrame(data2)
df_merge1=pd.merge(df1, df2, how='inner', on='EmployeeID')
print(df_merge1)
df_merge2=pd.merge(df1, df2, how='outer', on='EmployeeID')
print(df_merge2)
df_merge3=pd.merge(df1, df2, how='left', on='EmployeeID')
print(df_merge3)

