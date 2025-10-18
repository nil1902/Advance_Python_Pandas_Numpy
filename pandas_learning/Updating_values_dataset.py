#update the dataset value using loc and iloc
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
# Updating values using loc
df.loc[1, 'City'] = 'San Francisco'  # Update Bob's city || loc mean "label based indexing" or location
df.loc[3, 'performance_score'] = 98  # Update David's performance score
print("\nDataFrame after updating values using loc:")
print(df)
# Updating values using iloc
df.iloc[0, 2] = 'Boston'  # Update Alice's city
df.iloc[2, 4] = 90       # Update Charlie's performance score
print("\nDataFrame after updating values using iloc:")
print(df)
# Updating multiple values
df.loc[ df['Age'] > 25 , 'salary'] = df['salary'] * 1.05  # Increase salary by 5% for those older than 25
print("\nDataFrame after updating multiple values:")
print(df)

