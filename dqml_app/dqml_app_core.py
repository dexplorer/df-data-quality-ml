import pandas as pd
from datetime import datetime as dt
import xgboost as xgb
from sklearn.model_selection import train_test_split

from dqml_app import settings as sc
from dqml_app import dataset as ds
from dqml_app.app_calendar import eff_date as ed

# import data
from dqml_app.data_sample import sample as da
from dqml_app.feature_eng import features as fe
from dqml_app.explainability import explain as ex


def detect_anomalies(dataset_id: str) -> dict[str, float]:
    # Get dataset metadata
    datasets_json_file = f"{sc.api_data_path}/{sc.api_datasets_file}"
    dataset = ds.LocalDelimFileDataset.from_json(
        datasets_json_file, "datasets", dataset_id
    )

    # Get current effective date
    cur_date = ed.get_cur_eff_date(schedule_id=dataset.schedule_id)
    # Get current effective date
    prior_dates = ed.get_prior_eff_dates(
        schedule_id=dataset.schedule_id,
        snapshots=dataset.model_parameters.hist_data_snapshots,
    )

    # Get random samples of data for the specified dates
    data_current = da.query_random_sample(dataset=dataset, eff_date=cur_date)
    data_prior = pd.concat(
        [
            da.query_random_sample(dataset=dataset, eff_date=prior_date)
            for prior_date in prior_dates
        ],
        ignore_index=True,
    )
    print("Raw data")
    print(data_current)
    print(data_prior)

    # Create a binary response variable indicating the date
    y = [1] * len(data_current) + [0] * len(data_prior)

    # Concatenate the data ensuring the order of concatenation
    data_all = pd.concat([data_current, data_prior], ignore_index=True)

    # Determine the features to build based on the data columns
    feature_list = [
        (
            column,
            fe.determine_features(data_all=data_all, column=column, dataset=dataset),
        )
        for column in data_all.columns
    ]
    # print(feature_list)

    # Encode the features, here encode_feature returns a Dataframe
    encoded_features = [
        fe.encode_feature(data_all, column, feature)
        for column, feature in feature_list
        if feature != "not_a_feature"
    ]

    # Combine the encoded features into a single dataframe
    X = pd.concat(encoded_features, axis=1)
    print("Features")
    print(X)
    # print(X.dtypes)
    print("Target Labels")
    print(y)

    # Split data into training and test/evaluation sets
    X_train, X_eval, y_train, y_eval = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train a ML model using the features and response variable
    model = xgb.XGBClassifier(early_stopping_rounds=10)
    model.fit(X_train, y_train, eval_set=[(X_eval, y_eval)], verbose=False)

    # Obtain SHAP values to explain the model's predictions
    current_data_indices = [idx for idx, label_val in enumerate(y) if label_val == 1]
    # current_data_indices = [idx for idx, label_val in enumerate(y) if label_val == 1]
    data_for_prediction = X.loc[current_data_indices]
    # Get only a subset of observations for explainer
    # data_for_prediction = X.loc[current_data_indices].iloc[0:2]
    print("Data (Features) for prediction")
    print(data_for_prediction)

    # Get tree explainer
    explainer = ex.get_shap_tree_explainer(model)

    #Get shap values
    shap_values = ex.get_shap_values(explainer, data_for_prediction)
    print("SHAP values")
    print(shap_values)

    # Plot shap values
    ex.plot_shap_values(explainer, shap_values, data_for_prediction, dataset_id)

    # Compute anamoly scores for each column based on the SHAP values
    column_scores = ex.compute_column_scores(shap_values, feature_names=X.columns)

    return column_scores
