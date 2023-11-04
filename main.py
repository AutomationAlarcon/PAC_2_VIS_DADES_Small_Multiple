import pandas as pd

file_path = 'global_electricity_statistics.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)

print(df.head())
