import panda as pd
from pandas import Series, DataFrame
data1 = Series([6,77,888,9999])
data1.index
data2 = Series([8, 9, 11], index=["Joe", "Jane", "John"])
data2["Joe"]
data3["Joe"]
data2
data2 += 1
data2
data2[data2 > 10]
import numpy as np
np.random.rand(20)
data4 = Series(np.random.rand(20))
data4
data4[data4 <= 0.75]
data = {'school': ['Baxters', 'Racine'],'test scores': [90, 96]}
data
table = DataFrame(data, index =['School 1', 'School 2'])
table
data = {'name': ['James', 'Jane', 'John', 'Jake', 'Audrey'], 'sex': ['M', 'F', 'M', 'M', 'F']}
table1 = DataFrame(data)
table
datan= {'name' : ['James', 'Jane', 'John', 'Jake', 'Audrey'], 'sex' : ['M', 'F', 'M', 'M', 'F']}
table1 = DataFrame(datan)
table1
tablefull = DataFrame(datafull, columns=['name', 'age', 'sex', 'height'])
tablefull
tablefull.mean()
tablefull['height'].mean()