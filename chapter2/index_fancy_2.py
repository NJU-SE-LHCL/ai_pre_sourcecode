import numpy as np

np_ar = np.arange(32).reshape((8, 4))
fancy_ar = np_ar[[-4, -2, -1, -7]]
print('花式结果：\n{}'.format(fancy_ar))
