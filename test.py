

import build_dataframes as bdf
import pandas as pd
import sys


def merge_df_by_mean():
    a,b = bdf.build_lignan_urin_dfs()


    data = {}

    df = pd.concat((a, b), axis=1)
    for i in df.columns:
        data[i] = {}
        for j in df.index:
            data[i][j] = df[i].ix[j].mean()

    return pd.DataFrame(data)