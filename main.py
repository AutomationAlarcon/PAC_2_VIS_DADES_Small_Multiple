import pandas as pd

file_path = 'global_electricity_statistics.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)

df1 = df[["Country","Features","2016","2017","2018","2019","2020","2021"]]
values=["Canada","France", "Germany", "Italy", "Japan", "Russia", "United States", "United Kingdom"]
df2 = df1.loc[(df1["Country"].isin(values)) & (df1["Features"] == "net generation")]

print(df2)

