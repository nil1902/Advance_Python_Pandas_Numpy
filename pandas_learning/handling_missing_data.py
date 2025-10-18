# # NaN => Not a Number
# None => Python's null value
# isnull() => to detect missing values
# notnull() => to detect non-missing values
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, None, 22, 32],
    'City': ['New York', 'Los Angeles', None, 'Houston'],
    'salary': [70000, 80000, None, 90000],
    'performance_score': [88, 92, 85, None]
}
df = pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)
# Detecting missing values
print("\nMissing Values in DataFrame:")
print(df.isnull()) # isnull() function to detect missing values , false means value is present , true means value is missing
# Detecting non-missing values
print("\nNon-Missing Values in DataFrame:")
print(df.notnull()) # notnull() function to detect non-missing values , true means value is present , false means value is missing
# Handling missing values by filling with a specific value

# detect how many missing value are present 
print(df.isnull().sum())

print(df.describe())

df_filled = df.fillna({
    'Age': df['Age'].mean(),  # Fill missing Age with mean age  
    'City': 'Unknown',         # Fill missing City with 'Unknown'
    'salary': df['salary'].median(),  # Fill missing salary with median salary
    'performance_score': df['performance_score'].mean()  # Fill missing performance_score with mean score
})
print("\nDataFrame after Filling Missing Values:")
print(df_filled)

df.dropna(inplace=True)  # Drop rows with any missing values
print("\nDataFrame after Dropping Rows with Missing Values:")
print(df)
print(df.info()) #print summary of dataframe