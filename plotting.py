import util
import pandas as pd



def plot_per_index(df):
    for ix in df.index:
        index_df = util.test_person_series_to_df(df.ix[ix])
        plot_figure(index_df, ix)


def plot_figure(df, name):
    df.plot(title=name)


def plot_diff_btw_columns(df, column_a, column_b):
    get_diff_btw_columns(df, column_a, column_b).plot(kind='bar')


def get_diff_btw_columns(df, column_a, column_b):
    data = {}
    for test_person in range(1,10):
        build_column_a = str(test_person) + '-' + str(column_a)
        build_column_b = str(test_person) + '-' + str(column_b)

        data[test_person] = df[build_column_b] - df[build_column_a]

    return pd.DataFrame(data)



if __name__ == "__main__":
    import build_dataframes as bdf
    import matplotlib.pyplot as plt

    # @todo missing values
    lignan_urin_df = bdf.build_lignan_urin_dfs()[1]#.fillna(0)
    lignan_plasma_df = bdf.build_lignan_plasma_dfs()[1]#.fillna(0)
    #scfa_wet_df = bdf.build_scfa_wet_df()
    #scfa_dry_df = bdf.build_scfa_dry_df()
    #plot_per_index(scfa_dry_df)
    #plt.legend(loc='right')
    #plt.show()

    plot_diff_btw_columns(lignan_urin_df, 3, 4)
    plot_diff_btw_columns(lignan_plasma_df, 3, 4)
    #plot_diff_btw_columns(scfa_wet_df, 3, 4)
    #plot_diff_btw_columns(scfa_dry_df, 3, 4)
    plt.show()