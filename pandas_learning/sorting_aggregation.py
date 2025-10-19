#sorting -> df.sort_values(by=['column1','column2'], ascending=[True, False],inplace=True) 

import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 32],
    'City': ['New York', 'Los Angeles', "Delhi", 'Houston'],
    'salary': [70000, 80000, 75000, 90000],
    'performance_score': [88, 92, 85, 95]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Sorting the DataFrame by Age (ascending) and salary (descending)
df.sort_values(by="Age", ascending=False, inplace=True)
print("\nDataFrame after sorting by Age (ascending): ")
print(df)

multiple_sort_df = df.sort_values(by=['Age','salary'], ascending=[True, False])
print("\nDataFrame after sorting by Age (ascending) and salary (ascending): ") 
print(multiple_sort_df)


# aggregation mean performing aggregation operations like sum, mean, count, etc. on DataFrame columns
import pandas as pd

af=pd.DataFrame(data)
print("\nOriginal DataFrame for aggregation:")
print(af)
# Aggregation operations
mean_age = af['Age'].mean()
total_salary = af['salary'].sum()
performance_count = af['performance_score'].count()

print("\nMean Age:", mean_age)
print("Total Salary:", total_salary)
print("Count of Performance Scores:", performance_count)
# Multiple aggregation

agg_results = af.agg({
    'Age': ['mean', 'max', 'min'],  
    'salary': ['sum', 'mean'],
    'performance_score': ['count', 'mean']
})
print("\nAggregation Results:")
print(agg_results)
