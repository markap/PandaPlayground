import pandas as pd


def test_person_series_to_df(series):
    return series_to_df(series, lambda x: x.split('-'))


def series_to_df(series, split_fn):

    data = {}

    for idx in series.index:
        val = series[idx]

        new_index, new_column = split_fn(idx)

        if new_index in data:
            data[new_index][new_column] = val
        else:
            data[new_index] = {new_column: val}

    return pd.DataFrame(data)




def get_diff_btw_columns(df, column_a, column_b):
    data = {}
    for test_person in range(1,10):
        build_column_a = str(test_person) + '-' + str(column_a)
        build_column_b = str(test_person) + '-' + str(column_b)

        data[test_person] = df[build_column_b] - df[build_column_a]

    return pd.DataFrame(data)


def get_column(df, column):
    data = {}
    for test_person in range(1,10):
        build_column = str(test_person) + '-' + str(column)

        data[build_column] = df[build_column]

    return pd.DataFrame(data)


def normalize_by_sum(series):
    return series/float(series.sum())




def merge_dfs_by_mean(a,b):

    data = {}

    df = pd.concat((a, b), axis=1)
    for i in df.columns:
        data[i] = {}
        for j in df.index:
            data[i][j] = df[i].ix[j].mean()

    return pd.DataFrame(data)



def get_series_for_time_and_index(df, time, index):
    columns = []

    for person in range(1,10):
        for t in time:
            columns.append(str(person) + '-' + str(t))

    return df[columns].ix[index]
