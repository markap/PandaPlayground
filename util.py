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