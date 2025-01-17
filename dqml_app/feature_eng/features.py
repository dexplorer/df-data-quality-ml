import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from dqml_app import dataset as ds


def determine_features(data_all: pd.DataFrame, column: str, dataset: ds.Dataset):
    feature_name = "not_a_feature"
    for feature in dataset.model_parameters.features:
        if column == feature.column:
            if feature.encoding == "frequency":
                feature_name = f"{column}_freq_encode"
            elif feature.encoding == "one hot":
                feature_name = f"{column}_onehot_encode"
            else:
                feature_name = column
    return feature_name


def encode_feature(data_all: pd.DataFrame, column: str, feature: str) -> pd.DataFrame:
    if feature.endswith("_freq_encode"):
        feature_df = frequency_encoding(data_all, column, feature)
    elif feature.endswith("_onehot_encode"):
        feature_df = onehot_encoding(data_all, column, feature)
        feature_df.columns = [f"{column}_{c}" for c in feature_df.columns]
    else:
        feature_df = numeric_encoding(data_all, column, feature)

    return feature_df


def frequency_encoding(df: pd.DataFrame, column: str, feature: str):
    # grouping by frequency
    fq = df.groupby(column).size() / len(df)
    # mapping values to dataframe
    feature_df = df[column].map(fq)
    return feature_df


def onehot_encoding(df: pd.DataFrame, column: str, feature: str):
    enc = OneHotEncoder()
    # transforming the column after fitting
    enc = enc.fit_transform(df[[column]]).toarray()
    # converting arrays to a dataframe
    feature_df = pd.DataFrame(enc)
    return feature_df


def numeric_encoding(df: pd.DataFrame, column: str, feature: str):
    feature_df = pd.DataFrame(df[column].astype(float))
    # return feature_df
    return normalize_numeric_feature(df=feature_df, column=column)

def normalize_numeric_feature(df: pd.DataFrame, column: str):
    feature_df = df[column] / df[column].max()
    return feature_df