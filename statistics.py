import pandas as pd
import numpy as np


#pd.read_csv('test.csv', index_col=0).T.index

#pd.read_csv('test.csv', index_col=0).T['1-2-U-2']
#pd.read_csv('test.csv', index_col=0).T['1-2-U-2'].mean()

#pd.read_csv('test.csv', index_col=0).columns


""" reindex """
df = pd.read_csv('test.csv', index_col=0)
type(np.array_split(df,2)[0])



reindex = []

for i in df.index:
    reindex.append(i.replace("-", "_"))

print df.ix['1-2-U-2']
#df_reindexed = df.reindex(index=reindex, columns=df.columns)
#df
df_reindexed = pd.DataFrame(df.values, reindex, df.columns)
print df_reindexed.ix['1_2_U_2']


# copy values manually
#split2.from_records(split)

"""
>>> a = pd.read_csv('test.csv', index_col=0).T['1-2-U-2']
>>> b = pd.read_csv('test.csv', index_col=0).T['1-3-U-2']
>>> a.corr(b)
0.83486399269854028

"""
#pd.DataFrame(df.values, range(2,92), df.columns).index

