import util
import const
import os



def plot_per_index(df, path):

    for ix in df.index:
        index_df = util.test_person_series_to_df(df.ix[ix])
        #return index_df

        fig = get_plot_figure(index_df, ix)
        fig.savefig(get_path(path, ix))

        fig = get_plot_figure(index_df[range(1,6)], ix)
        fig.savefig(get_path(path, ix, '_part1'))

        fig = get_plot_figure(index_df[range(6,10)], ix)
        fig.savefig(get_path(path, ix, '_part2'))


def get_path(folder, ix, info='', file_type='png'):
    if not os.path.exists(const.VISUALIZATION + folder):
        os.makedirs(const.VISUALIZATION + folder)

    ix = ''.join(e for e in ix if e.isalnum())
    return const.VISUALIZATION + folder + '/' + ix + info + '.' + file_type

def get_plot_figure(df, name):
    return df.plot(title=name).get_figure()


def plot_diff_btw_columns(df, column_a, column_b):
    return util.get_diff_btw_columns(df, column_a, column_b).plot(kind='bar').get_figure()


def plot_column(df, column):
    return util.get_column(df, column).plot(kind='bar').get_figure()


def plot_all_columns(df, name):
    for i in range(1,6):
        fig = plot_column(df, i)
        fig.subplots_adjust(bottom=0.2)
        fig.savefig(get_path(name, "column", str(i)))

def plot_all_diffs_btw_columns(df, name):
    for i in range(1,5):
        fig = plot_diff_btw_columns(df, i, i+1)
        fig.subplots_adjust(bottom=0.2)
        fig.savefig(get_path(name, 'diff', str(i) + '_' + str(i+1)))


def plot_all(df, name):
    plot_per_index(df, name)
    plot_all_columns(df, name)
    plot_all_diffs_btw_columns(df, name)
    print "plot all for %s done" % name


def plot_all_otus():
    import df_reader as dfr
    import matplotlib.pyplot as plt
    fig = dfr.otus_df().T.plot().get_figure()
    plt.legend(loc="upper left", bbox_to_anchor=(1,1))

    fig.savefig(get_path('otus', 'all'))



if __name__ == "__main__":
    import df_reader as dfr
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.rcParams.update({'font.size': 6})

    df = dfr.scfa_wet_df()
    plot_all(df, 'scfa_wet')
    #plot_diff_btw_columns(df, 3, 4)
    #plt.subplots_adjust(bottom=0.2)








