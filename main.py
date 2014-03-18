import preprocessing as bdf
import otu_differences as otu_diff
import plotting
import matplotlib.pyplot as plt



def otu_dissimilarity_matrix():
    df = bdf.build_otu_df()
    matrix, _ = otu_diff.compute_similarity_matrix(df)
    print matrix


def plot_otu_main_differences(range_cb=lambda x: x[0:5], column=3):
    df = bdf.build_otu_df()
    _, main_values = otu_diff.compute_similarity_matrix(df)

    main_diff_otus = otu_diff.compute_main_diff_otus(main_values)
    sorted_otus = main_diff_otus.T.sort('count', ascending=False).index
    #print sorted_otus
    plotting.plot_column(df.ix[list(range_cb(sorted_otus))], column)
    plt.show()


def plot_lignan_urin_diff(column_a = 3, column_b = 4):
    lignan_urin_df = bdf.build_lignan_urin_df()
    plotting.plot_diff_btw_columns(lignan_urin_df, column_a, column_b)
    plt.show()

def plot_lignan_urin_column(column):
    lignan_urin_df = bdf.build_lignan_urin_df()
    plotting.plot_column(lignan_urin_df, column)
    plt.show()

def plot_lignan_plasma_diff(column_a = 3, column_b = 4):
    lignan_plasma_df = bdf.build_lignan_plasma_df()
    plotting.plot_diff_btw_columns(lignan_plasma_df, column_a, column_b)
    plt.show()


def plot_lignan_plasma_column(column):
    lignan_plasma_df = bdf.build_lignan_plasma_df()
    plotting.plot_column(lignan_plasma_df, column)
    plt.show()


def plot_scfa_wet_diff(column_a = 3, column_b = 4):
    scfa_wet_df = bdf.build_scfa_wet_df()
    plotting.plot_diff_btw_columns(scfa_wet_df, column_a, column_b)
    plt.show()


def plot_scfa_wet_column(column):
    scfa_wet_df = bdf.build_scfa_wet_df()
    plotting.plot_column(scfa_wet_df, column)
    plt.show()


def plot_scfa_dry_diff(column_a = 3, column_b = 4):
    scfa_dry_df = bdf.build_scfa_dry_df()
    plotting.plot_diff_btw_columns(scfa_dry_df, column_a, column_b)
    plt.show()


def plot_scfa_dry_column(column):
    scfa_dry_df = bdf.build_scfa_dry_df()
    plotting.plot_column(scfa_dry_df, column)
    plt.show()


def plot_blood_lipid_diff(column_a = 3, column_b = 4):
    blood_lipid_df = bdf.build_blood_lipid_df()
    plotting.plot_diff_btw_columns(blood_lipid_df, column_a, column_b)
    plt.show()


def plot_blood_lipid_column(column):
    blood_lipid_df = bdf.build_blood_lipid_df()
    plotting.plot_column(blood_lipid_df, column)
    plt.show()


def plot_blood_lipid_per_index():
    blood_lipid_df = bdf.build_blood_lipid_df()
    plotting.plot_per_index(blood_lipid_df)
    plt.show()

def plot_lignan_urin_per_index():
    lignan_urin_df = bdf.build_lignan_urin_df()
    plotting.plot_per_index(lignan_urin_df)
    plt.show()


def plot_lignan_plasma_per_index():
    lignan_plasma_df = bdf.build_lignan_plasma_df()
    plotting.plot_per_index(lignan_plasma_df)
    plt.show()


def plot_scfa_wet_per_index():
    scfa_wet_df = bdf.build_scfa_wet_df()
    plotting.plot_per_index(scfa_wet_df)
    plt.show()


def plot_scfa_dry_per_index():
    scfa_dry_df = bdf.build_scfa_dry_df()
    plotting.plot_per_index(scfa_dry_df)
    plt.show()

def plot_nutrition(nutrition=None):
    nutrition_df = bdf.build_nutrition_df()

    if nutrition:
        nutrition_df.ix[nutrition].plot(kind='bar')
    else:
        nutrition_df.plot(kind='bar')

    plt.show()


def get_nutrition_types():
    return dict([(k,v) for k,v in enumerate(bdf.build_nutrition_df().index)])
