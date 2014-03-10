import build_dataframes as bdf

def abs_diff(x, y):
    return abs(x - y)


df = bdf.build_otu_df().T

diff_1 = abs_diff(df['2-3'], df['2-4'])
diff_1.sort(ascending=False)

print diff_1[:10]

print df['1-3'][diff_1.index[0]]
print df['1-4'][diff_1.index[0]]

print df['2-3'][diff_1.index[0]]
print df['2-4'][diff_1.index[0]]

print df['3-3'][diff_1.index[0]]
print df['3-4'][diff_1.index[0]]

print df['4-3'][diff_1.index[0]]
print df['4-4'][diff_1.index[0]]

print df['5-3'][diff_1.index[0]]
print df['5-4'][diff_1.index[0]]