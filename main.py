import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'global_electricity_statistics.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)

df1 = df[["Country","Features","2016","2017","2018","2019","2020","2021"]]
legend_value = list(df1.columns.values)
legend_value = legend_value[2:]
print(legend_value)

x1 = ["United States", "Russia", "Canada","France", "Germany", "Italy", "Japan", "United Kingdom"]
df2 = df1.loc[(df1["Country"].isin(x1)) & (df1["Features"] == "net generation")]
x = list(df2["Country"])
print(df2)
print(x)

df2['Country'] = df2['Country'].astype('category')
df2['Features'] = df2['Features'].astype('category')
df2['2016'] = df2['2016'].astype(float)
df2['2017'] = df2['2017'].astype(float)
df2['2018'] = df2['2018'].astype(float)
df2['2019'] = df2['2019'].astype(float)
df2['2020'] = df2['2020'].astype(float)
df2['2021'] = df2['2021'].astype(float)

print(df2.dtypes)

y = [list(df2["2016"]), list(df2["2017"]), list(df2["2018"]), list(df2["2019"]), list(df2["2020"]), list(df2["2021"])]

plt.figure(figsize=(15, 12))
for i in range(len(y)):
    print(i)
    print(y[i])
    plt.subplot(3, 2, i+1)
    #plt.plot(x, y[i], label=legend_value[i], marker='X')
    plt.barh(x, y[i], color='gray')
    plt.title(legend_value[i])
    plt.ylabel("G8 Countries")
    plt.xlabel("Net generation (billion kWh)")
    #plt.legend(loc="upper left")
    plt.xticks(rotation='horizontal')
    #plt.yticks(np.arange(0, 5000, 1000))
    plt.grid(color='k', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.savefig("g8_net_generation", dpi=100, bbox_inches='tight')


