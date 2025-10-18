# sample data set build 
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
print(df.describe()) #print summary of dataframe
print(df.shape) #print shape of dataframe
print(df.columns) #print columns of dataframe
print(df.dtypes) #print data types of each column