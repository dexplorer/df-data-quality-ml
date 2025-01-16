import pandas as pd 
import datetime as dt 
import xgboost as xgb 
from sk_learn.model_selection import train_test_split 
from shap import TreeExplainer 

# import data 
from data_access import sample as da 
from feature_eng import features as fe 
from explainability import explain as ex 

def detect_anomalies(dataset_id: str) -> dict[str, float]:
    # Get dataset metadata 
    datasets_json_file = f"{sc.api_data_path}/{sc.api_datasets_file}"
    dataset = ds.LocalDelimFileDataset.from_json(
        datasets_json_file, "datasets", dataset_id
    )

    # Get current effective date
    cur_date = ed.get_cur_eff_date(schedule_id=dataset.schedule_id)
    # Get current effective date
    prior_dates = ed.get_prior_eff_dates(schedule_id=dataset.schedule_id, snapshots=dataset.dqml.mdl_hist_data_dates)

    # Get random samples of data for the specified dates
    data_current = da.query_random_sample(dataset_id=dataset_id, eff_date=cur_date)
    data_prior = [da.query_random_sample(dataset_id=dataset_id, eff_date=prior_date) for prior_date in prior_dates]
    
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
    
    # Combine the encoded features into a single dataframe
    X = pd.concat(encoded_features, axis=1)

