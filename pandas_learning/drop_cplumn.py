import pandas as pd
data={
    'Name':['Alice','Bob','Charlie','David'], 
    'Age':[24,27,22,32],
    'City':['New York','Los Angeles','Chicago','Houston'],
    'salary':[70000,80000,60000,90000],
    'performance_score':[88,92,85,95]
}
df = pd.DataFrame(data)
print(df)
# Dropping a single column
df_dropped = df.drop('City', axis=1)  # axis=1 indicates column
print("\nDataFrame after dropping 'City' column:")  
print(df_dropped)

#multiple columns drop
df_dropped_multiple = df.drop(['Age', 'salary'], inplace=True, axis=1) # inplace=True means changes will be applied to original dataframe
print("\nDataFrame after dropping 'Age' and 'salary' columns:")  # axis=1 indicates column and axis=0 indicates row
print(df) 