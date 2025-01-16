import pandas as pd 
import datetime as dt 
import xgboost as xgb 
from sk_learn.model_selection import train_test_split 
from shap import TreeExplainer 

# import data 
from data_access import sample as da 
from feature_eng import features as fe 
from explainability import explain as ex 

def detect_anomalies(table: str, time_column: str, cur_date: dt.date, prior_date: dt.date, sample_size: int) -> dict[str, float]:
    # Get random samples of data for the specified dates
    data_current = da.query_random_sample(table='ticket', time_column='listtime', eff_date=cur_date, sample_size=sample_size)
    data_prior = da.query_random_sample(table='ticket', time_column='listtime', eff_date=prior_date, sample_size=sample_size)
    
    # Create a binary response variable indicating the date
    y = [1] * len(data_current) + [0] * len(data_prior)

    # Concatenate the data ensuring the order of concatenation 
    data_all = pd.concat([data_current, data_prior], ignore_index=True)
    
    # Determine the features to build based on the data columns
    feature_list = {
        column: fe.determine_features(data_all, column) for column in data_all.columns 
    } 

    # Encode the features, here encode_feature returns a Dataframe 
    encoded_features = [
        fe.encode_feature(data_all, column, feature) for column, feature in feature_list 
    ]
    