import util
import sys
import const
import pandas as pd
import matplotlib.pyplot as plt


class Correlation:

    def __init__(self, df_a, df_b, time=[1]):
        self.df_a = df_a
        self.df_b = df_b
        self.time = time
        self.ranks_ = None
        self.result_df = None
        self.ranked = None

        self.has_time_a = True
        self.has_time_b = True

        """ some datasets, e.g. nutrition have no time """
        if len(df_a.columns) == const.TEST_PERSONS or len(df_b.columns) == const.TEST_PERSONS:
            if len(time) != 1:
                print "no time axis"
                sys.exit()

            if len(df_a.columns) == const.TEST_PERSONS:
                self.has_time_a = False

            if len(df_b.columns) == const.TEST_PERSONS:
                self.has_time_b = False




    def compute_matrix(self):

        result = {}

        column_index_a = util.get_column_index(self.time, self.has_time_a)
        column_index_b = util.get_column_index(self.time, self.has_time_b)

        for index_a in self.df_a.index:

            result[index_a] = {}
            series_a = self.df_a[column_index_a].ix[index_a]

            for index_b in self.df_b.index:

                series_b = self.df_b[column_index_b].ix[index_b]
                """ sometimes the index is different, e.g. nutrition dataset """
                series_b = pd.Series(series_b.values, index=series_a.index)

                result[index_a][index_b] = series_a.corr(series_b)

        self.result_df = pd.DataFrame(result)
        return self.result_df


    def ranks(self, ranks=10):
        if self.ranks_ is None:
            if not self.result_df:
                print "compute matrix first"
                return

            df = self.result_df.stack()
            absolute_ranks = abs(df)
            absolute_ranks.sort(ascending=False)

            ranked = []
            for idx in absolute_ranks.index:
                ranked.append([idx, df[idx]])

            self.ranks_ = pd.Series(ranked)
            self.ranked = ranked
        return pd.DataFrame(self.ranked[:ranks])


    def plot_rank(self, rank=0):

        index_a, index_b, series_a, series_b = self.__get_series_to_plot(rank)

        df = pd.DataFrame(series_a, columns=[index_a])
        df[index_b] = series_b

        df.plot()
        plt.show()


    def scatterplot_rank(self, rank=0):

        index_a, index_b, series_a, series_b = self.__get_series_to_plot(rank)
        plt.scatter(series_a, series_b)
        plt.xlabel(index_a)
        plt.ylabel(index_b)
        plt.show()


    def stats_of_rank(self, rank=0):
        index_a, index_b, series_a, series_b = self.__get_series_to_plot(rank)
        print index_a, index_b

        print "correlation is %f" % series_a.corr(series_b)

        import scipy.stats
        print scipy.stats.ttest_ind(series_a, series_b)



    def __get_series_to_plot(self, rank):
        if self.ranks_ is None:
            if not self.result_df:
                print "compute matrix first"
                return
            self.ranks()


        index_b, index_a = self.ranks_[rank][0]

        return self.__get_series_to_plot_by_index(index_a, index_b)

    def __get_series_to_plot_by_index(self, index_a, index_b):

        column_index_a = util.get_column_index(self.time, self.has_time_a)
        column_index_b = util.get_column_index(self.time, self.has_time_b)

        series_a = self.df_a[column_index_a].ix[index_a]
        series_b = self.df_b[column_index_b].ix[index_b]

        """ sometimes the index is different, e.g. nutrition dataset """
        series_b = pd.Series(series_b.values, index=series_a.index)

        return index_a, index_b, series_a, series_b


def scfa_wet_to_otus_correlation(time=[1]):
    import df_reader as dfr
    a = dfr.scfa_wet_df()
    b = dfr.otus_df()

    return Correlation(a,b,time)



def lignan_urin_to_otus_correlation(time=[1]):
    import df_reader as dfr
    a = dfr.lignan_urin_df()
    b = dfr.otus_df()

    return Correlation(a,b,time)


def nutrition_to_otus_correlation(time=[1]):
    import df_reader as dfr
    a = dfr.nutrition_df()
    b = dfr.otus_df()

    return Correlation(a,b,time)



if __name__ == '__main__':
    obj = nutrition_to_otus_correlation(time=[1])
    obj.compute_matrix()
    obj.ranks(40).to_csv('outi.csv')
