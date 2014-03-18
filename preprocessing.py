import pandas as pd
import numpy as np
import const
import util


def reindex_df(df, split_fn):
    reindex = []

    for i in df.index:
        index_parts = split_fn(i)

        """ index 6 is missing """
        test_person = index_parts[0] if int(index_parts[0]) < 6 else str(int(index_parts[0])-1)
        reindex.append(test_person + '-' + index_parts[1])

    return pd.DataFrame(df.values, reindex, df.columns).T


def build_lignan_urin_df():
    return build_lignan_df(const.ORG_LIGNAN_URIN_PATH, lambda x: x.split('-'))


def build_lignan_plasma_df():
    return build_lignan_df(const.ORG_LIGNAN_PLASMA_PATH, lambda x: x.split()[-1].split('-'))


def build_lignan_df(file_, split_fn):
    temporary_df = pd.read_csv(file_, index_col=0).fillna(0)
    temporary_df = temporary_df.applymap(lambda x: x if x > 0 else 0)


    a,b = np.array_split(temporary_df,2)
    df = util.merge_dfs_by_mean(a,b)

    return reindex_df(df, split_fn)


def build_nutrition_df():
    temporary_df = pd.read_csv(const.ORG_NUTRITION_PATH, index_col=0)

    reindex = []
    for i in temporary_df.index:
        test_person = int(i.split('-')[1])
        """ index 6 is missing """
        test_person = test_person if test_person < 6 else test_person-1
        reindex.append(str(test_person))

    return pd.DataFrame(temporary_df.values, reindex, temporary_df.columns).T


def build_otu_df():

    temporary_df = pd.read_csv(const.ORG_OTU_PATH, delimiter='\t', index_col=0).T[:-1].astype(int)

    return reindex_df(temporary_df, lambda x: x.split('.')).sort_index(axis=1)


def build_scfa_wet_df():
    return build_scfa_df(const.ORG_SCFA_WET_PATH)


def build_scfa_dry_df():
    return build_scfa_df(const.ORG_SCFA_DRY_PATH)

def build_scfa_df(path):
    temporary_df = pd.read_csv(path, index_col=0)
    return reindex_df(temporary_df, lambda x: x.split('-'))


def build_blood_lipid_df():
    import csv

    lipid_data_container = {}

    with open(const.ORG_BLOOD_LIPID_PATH, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = None
        for i, row in enumerate(reader):
            if i % 10 == 0:
                header = row
                lipid_data = {}
            else:
                test_person = None

                for j, item in enumerate(row):
                    if j == 0:
                        test_person = int(item.split('-')[-1])

                        """ index 6 is missing """
                        test_person = test_person if test_person < 6 else test_person-1
                    else:
                        lipid_data[str(test_person) + '-' + str(j)] = float(item)

                lipid_data_container[header[0]] =  lipid_data

        return pd.DataFrame(lipid_data_container).T



if __name__ == "__main__":
    build_blood_lipid_df().to_csv(const.BLOOD_LIPID_PATH)
    build_lignan_plasma_df().to_csv(const.LIGNAN_PLASMA_PATH)
    build_lignan_urin_df().to_csv(const.LIGNAN_URIN_PATH)
    build_scfa_dry_df().to_csv(const.SCFA_DRY_PATH)
    build_scfa_wet_df().to_csv(const.SCFA_WET_PATH)
    build_otu_df().to_csv(const.OTUS_PATH)
    build_nutrition_df().to_csv(const.NUTRITION_PATH)

    print "preprocessed files written"

