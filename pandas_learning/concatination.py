# dataframe concatenation in pandas is the process of combining two or more DataFrames along a particular axis (either rows or columns). This is useful when you have multiple datasets that you want to analyze together.
# both horizontally and vertically
#  axis 1 for columns (horizontal) and axis 0 for rows (vertical)
import pandas as pd
# Creating sample DataFrames
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22]
}
data2 = {
    'Name': ['David', 'Eve', 'Frank'],
    'Age': [32, 28, 26]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
# Concatenating DataFrames vertically (along rows)
vertical_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nVertical Concatenation (along rows):")
print(vertical_concat)
# Concatenating DataFrames horizontally (along columns)
horizontal_concat = pd.concat([df1, df2], axis=1)
print("\nHorizontal Concatenation (along columns):")
print(horizontal_concat)