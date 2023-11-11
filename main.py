import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'global_electricity_statistics.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)

df1 = df[["Country","Features","2016","2017","2018","2019","2020","2021"]]
x1 = ["United States", "Canada","France", "Germany", "Italy", "Japan", "United Kingdom"]

df_net_consumption = df1.loc[(df1["Country"].isin(x1)) & (df1["Features"] == "net consumption")]
df_imports = df1.loc[(df1["Country"].isin(x1)) & (df1["Features"] == "imports")]
df_exports = df1.loc[(df1["Country"].isin(x1)) & (df1["Features"] == "exports")]
df_net_imports = df1.loc[(df1["Country"].isin(x1)) & (df1["Features"] == "net imports")]
df_net_exports = df1.loc[(df1["Country"].isin(x1)) & (df1["Features"] == "net exports")]
df_net_generation = df1.loc[(df1["Country"].isin(x1)) & (df1["Features"] == "net generation")]
x = list(df_net_generation["Country"])
print(df_net_generation)
print(x)

df_net_generation['Country'] = df_net_generation['Country'].astype('category')
df_net_generation['Features'] = df_net_generation['Features'].astype('category')
df_net_generation['2016'] = df_net_generation['2016'].astype(float)
df_net_generation['2017'] = df_net_generation['2017'].astype(float)
df_net_generation['2018'] = df_net_generation['2018'].astype(float)
df_net_generation['2019'] = df_net_generation['2019'].astype(float)
df_net_generation['2020'] = df_net_generation['2020'].astype(float)
df_net_generation['2021'] = df_net_generation['2021'].astype(float)

print(df_net_generation.dtypes)

# df_net_consumption['2021'] = df_net_consumption['2021'].astype(float)
# df_imports['2021'] = df_imports['2021'].astype(float)
# df_exports['2021'] = df_exports['2021'].astype(float)
# df_net_imports['2021'] = df_net_imports['2021'].astype(float)
# df_net_exports['2021'] = df_net_exports['2021'].astype(float)

# y = [list(df_net_generation["2021"]), list(df_net_consumption["2021"]), list(df_imports["2021"]),
#      list(df_exports["2021"]), list(df_net_imports["2021"]), list(df_net_exports["2021"])]
# legend_value = ["Net generation", "Net consumption", "Imports", "Exports", "Net imports", "Net exports"]

y = [list(df_net_generation["2016"]), list(df_net_generation["2017"]), list(df_net_generation["2018"]),
     list(df_net_generation["2019"]), list(df_net_generation["2020"]), list(df_net_generation["2021"])]
legend_value = list(df1.columns.values)
legend_value = legend_value[2:]
print(legend_value)

plt.figure(figsize=(15, 12))
for i in range(len(y)):
    print(i)
    print(y[i])
    plt.subplot(3, 2, i+1)
    #plt.plot(x, y[i], label=legend_value[i], marker='X')
    bars = plt.barh(x, y[i], color='gray')
    plt.title("Net electricity generation in the year " + legend_value[i])
    plt.ylabel("G7 Countries")
    plt.xlabel("Net electricity generation (billion kWh)")
    #plt.legend(loc="lower right")
    plt.xticks(rotation='horizontal')
    plt.xticks(np.arange(0, 5500, 500))
    plt.grid(color='k', linestyle='--', linewidth=0.5)

    for bar in bars:
        xval = bar.get_width()
        plt.text(xval + 0.05, bar.get_y() + bar.get_height() / 2, round(xval, 2), ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.savefig("g7_net_generation", dpi=100, bbox_inches='tight')


