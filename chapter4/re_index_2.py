import pandas as pd
import numpy as np

df_1 = pd.DataFrame(np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
df_2 = pd.DataFrame(np.random.randn(2, 3), columns=['col1', 'col2', 'col3'])
print('NAN值填充：\n{}'.format(df_2.reindex_like(df_1)))
print("用前面的值填充NAN：\n{}".format(df_2.reindex_like(df_1, method='ffill')))
