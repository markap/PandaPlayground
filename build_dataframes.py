import pandas as pd
import numpy as np
import const


def reindex_df(df, split_fn):
    reindex = []

    for i in df.index:
        index_parts = split_fn(i)

        """ index 6 is missing """
        test_person = index_parts[0] if int(index_parts[0]) < 6 else str(int(index_parts[0])-1)
        reindex.append(test_person + '-' + index_parts[1])

    return pd.DataFrame(df.values, reindex, df.columns).T


def build_lignan_urin_dfs():
    return build_lignan_dfs(const.LIGNAN_URIN_PATH, lambda x: x.split('-'))


def build_lignan_plasma_dfs():
    return build_lignan_dfs(const.LIGNAN_PLASMA_PATH, lambda x: x.split()[-1].split('-'))


def build_lignan_dfs(file_, split_fn):
    temporary_df = pd.read_csv(file_, index_col=0)

    sample_a, sample_b = np.array_split(temporary_df,2)

    # todo add some assertions
    return reindex_df(sample_a, split_fn), reindex_df(sample_b, split_fn)


def build_nutrition_df():
    temporary_df = pd.read_csv(const.NUTRITION_PATH, index_col=0)

    reindex = []
    for i in temporary_df.index:
        test_person = int(i.split('-')[1])
        """ index 6 is missing """
        test_person = test_person if test_person < 6 else test_person-1
        reindex.append(str(test_person))

    return pd.DataFrame(temporary_df.values, reindex, temporary_df.columns).T


def build_otu_df():
    temporary_df = pd.read_csv(const.OTU_PATH, delimiter='\t', index_col=0).T

    def reindex_split(idx):
        new_index = idx.split('F')[0]
        return [new_index[:-1], new_index[-1]]
    return reindex_df(temporary_df, reindex_split)


def build_scfa_wet_df():
    return build_scfa_df(const.SCFA_WET_PATH)


def build_scfa_dry_df():
    return build_scfa_df(const.SCFA_DRY_PATH)

def build_scfa_df(path):
    temporary_df = pd.read_csv(path, index_col=0)
    return reindex_df(temporary_df, lambda x: x.split('-'))


def build_blood_lipid_df():
    import csv

    lipid_data_container = {}

    with open(const.BLOOD_LIPID_PATH, 'rb') as csvfile:
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
    lingnan_urin_a_df, lignan_urin_b_df = build_lignan_urin_dfs()
    #print lingnan_urin_a_df
    #print lignan_urin_b_df

    nutrition_df = build_nutrition_df()
    #print nutrition_df.columns
    #print nutrition_df.index

    lingnan_plasma_a_df, lignan_plasma_b_df = build_lignan_plasma_dfs()
    #print lingnan_plasma_a_df
    #print lignan_plasma_b_df

    blood_lipid_df = build_blood_lipid_df()
    print blood_lipid_df.index

    otu_df = build_otu_df()
    print otu_df.index

    scfa_dry_df = build_scfa_dry_df()
    scfa_wet_df = build_scfa_wet_df()
    print scfa_wet_df.index


