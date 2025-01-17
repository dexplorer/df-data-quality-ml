import pandas as pd
import numpy as np


def compute_column_scores(shap_values, feature_names: list):
    df = pd.DataFrame(shap_values, columns=feature_names)
    vals = np.abs(df.values).mean(0)

    shap_importance = pd.DataFrame(
        list(zip(feature_names, vals)), columns=["feature_name", "feature_importance"]
    )
    shap_importance.sort_values(
        by=["feature_importance"], ascending=False, inplace=True
    )
    # shap_importance.head()
    column_scores = shap_importance

    return column_scores
