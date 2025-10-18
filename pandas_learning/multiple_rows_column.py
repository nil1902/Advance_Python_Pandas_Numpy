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

print("\n")
print(df["Name"])  # Accessing single column

print("\n")
subset = df[['Name', 'Age','salary']]  # Accessing multiple columns
print(subset)
print("\n")

#rows filtering based on  single condition
print("\n")
high_salary = df[df['salary'] > 75000]
print(high_salary)

# filtering rows based on multiple conditions
print("\n")

filtered_data = df[(df['Age'] > 25) & (df['performance_score'] >= 90)]
print(filtered_data)
print("\n" )
filtered_data_two = df[(df['Age'] > 25) | (df['performance_score'] >= 50)]
print(filtered_data_two)