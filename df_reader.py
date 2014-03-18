import pandas as pd
import const

def blood_lipid_df():
    return __read_csv(const.BLOOD_LIPID_PATH)

def lignan_urin_df():
    return __read_csv(const.LIGNAN_URIN_PATH)

def lignan_plasma_df():
    return __read_csv(const.LIGNAN_PLASMA_PATH)

def scfa_wet_df():
    return __read_csv(const.SCFA_WET_PATH)

def scfa_dry_df():
    return __read_csv(const.SCFA_DRY_PATH)

def otus_df():
    return __read_csv(const.OTUS_PATH)

def nutrition_df():
    return __read_csv(const.NUTRITION_PATH)


def __read_csv(path):
    return pd.read_csv(path, index_col=0)