#group by 
import pandas as pd
data = {    
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance'],
    'Salary': [70000, 80000, 75000, 72000, 90000, 85000],
    'Performance_Score': [88, 92, 85, 90, 95, 87]
}   
df = pd.DataFrame(data)
print("Original DataFrame:")    
print(df)
# Grouping by Department and calculating mean Salary and Performance_Score
grouped_df = df.groupby("Department")["Salary"].sum()
print("\nGrouped DataFrame by Department with mean Salary and Performance_Score:")
print(grouped_df)   
multiple_grouped_df = df.groupby("Department").agg({
    'Salary': 'mean',   
    'Performance_Score': 'mean'
})
print("\nMultiple Aggregations (mean) on grouped DataFrame:")
print(multiple_grouped_df)



# some common aggregation function 
# Common aggregation functions in pandas:
# 1. sum() - Calculates the sum of values.  
# 2. mean() - Calculates the mean (average) of values.
# 3. count() - Counts the number of non-null values.
# 4. min() - Finds the minimum value.
# 5. max() - Finds the maximum value.
# 6. std() - Calculates the standard deviation of values.
# Example of using common aggregation functions
