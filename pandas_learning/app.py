import pandas as pd
df=pd.read_csv("sample.csv")    
print(df.head())
print("\n")
print(df.info()) #print summary of dataframe

cd=pd.read_excel("sample.xlsx")
print(cd.tail())
print("\n")
md= pd.read_json("sample.json")
print(md.describe())
print(md)