import build_dataframes as bdf
import util
import pandas as pd
import matplotlib.pyplot as plt


def compute_lignan_correlation(time=[1], lignan='EL'):

    lignan_urin_df = bdf.build_lignan_urin_df()
    return compute_correlation(lignan_urin_df, time, lignan)


def compute_scfa_correlation(time=[1], scfa='Butyric acid'):
    scfa_dry_df = bdf.build_scfa_dry_df()
    return compute_correlation(scfa_dry_df, time, scfa)


def compute_correlation(df, time, ix):
    otus_df = bdf.build_otu_df()

    series = util.get_series_for_time_and_index(df, time, ix)
    #lignan_series = util.normalize_by_sum(lignan_series)

    data = {}

    for otu in otus_df.index:
        otu_series = util.get_series_for_time_and_index(otus_df, time, otu)
        #otu_series = util.normalize_by_sum(otu_series)

        corr = otu_series.corr(series)

        data[otu] = {'corr': corr,
                     'abs': abs(corr)}

    return pd.DataFrame(data).T.sort('abs')['corr']




def plot_lignan_correlation(otu, time=[1], lignan='EL'):

    otu_series, lignan_series = get_lignan_correlation_series(otu, time, lignan)


    df = pd.DataFrame(otu_series, columns=[otu])
    df[lignan] = lignan_series

    df.plot()
    plt.show()


def plot_scfa_correlation(otu, time=[1], scfa='Butyric acid'):

    otu_series, scfa_series = get_scfa_correlation_series(otu, time, scfa)


    df = pd.DataFrame(otu_series, columns=[otu])
    df[scfa] = scfa_series

    df.plot()
    plt.show()


def scatterplot_scfa_correlation(otu, time=[1], scfa='Butyric acid'):
    otu_series, scfa_series = get_scfa_correlation_series(otu, time, scfa)
    plt.scatter(otu_series, scfa_series)
    plt.show()


def scatterplot_lignan_correlation(otu, time=[1], lignan='EL'):
    otu_series, lignan_series = get_lignan_correlation_series(otu, time, lignan)
    plt.scatter(otu_series, lignan_series)
    plt.show()


def get_lignan_correlation_series(otu, time=[1], lignan='EL'):

    lignan_urin_df = bdf.build_lignan_urin_df()
    return get_correlation_series(lignan_urin_df, otu, time, lignan)


def get_scfa_correlation_series(otu, time=[1], scfa='Butyric acid'):

    scfa_df = bdf.build_scfa_dry_df()
    return get_correlation_series(scfa_df, otu, time, scfa)




def get_correlation_series(df, otu, time, ix):
    otus_df = bdf.build_otu_df()

    #return util.normalize_by_sum(util.get_series_for_time_and_index(otus_df, time, otu)), \
        #util.normalize_by_sum(util.get_series_for_time_and_index(lignan_urin_df, time, lignan))

    return util.get_series_for_time_and_index(otus_df, time, otu), \
        util.get_series_for_time_and_index(df, time, ix)



def correlate_lignan_series(otu, time=[1], lignan='EL'):
    otus_series, lignan_series = get_lignan_correlation_series(otu, time, lignan)
    return otus_series.corr(lignan_series)


def correlate_scfa_series(otu, time=[1], scfa='Butyric acid'):
    otus_series, scfa_series = get_scfa_correlation_series(otu, time, scfa)
    return otus_series.corr(scfa_series)


