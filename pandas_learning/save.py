import pandas as pd
data={
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[24,27,22,32],
    'City':['New York','Los Angeles','Chicago','Houston']
}
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)
print(df) 
print(df.info()) #print summary of dataframe
df.to_excel('output.xlsx', index=False)
df.to_json('output.json', orient='records', lines=True)