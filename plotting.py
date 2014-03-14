import util
import pandas as pd



def plot_per_index(df):
    for ix in df.index:
        index_df = util.test_person_series_to_df(df.ix[ix])
        plot_figure(index_df, ix)


def plot_figure(df, name):
    df.plot(title=name)


def plot_diff_btw_columns(df, column_a, column_b):
    util.get_diff_btw_columns(df, column_a, column_b).plot(kind='bar')


def plot_column(df, column):
    util.get_column(df, column).plot(kind='bar')



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