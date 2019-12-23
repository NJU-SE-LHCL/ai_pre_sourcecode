import pandas as pd

df_data = {'Team': ['A', 'B', 'C', 'B', 'A', 'D', 'C'],
           'Rank': [1, 2, 2, 3, 3, 4, 1],
           'Year': [2018, 2019, 2020, 2019, 2018, 2020, 2021],
           'Points': [87.5, 81, 86, 79.5, 76, 89, 75]}
df = pd.DataFrame(df_data)
print('按一列分组：\n{}'.format(df.groupby('Team').groups))
print('按多列分组：\n{}'.format(df.groupby(['Team', 'Year']).groups))
