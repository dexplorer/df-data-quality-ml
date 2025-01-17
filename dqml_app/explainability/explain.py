def compute_column_scores(shap_values, feature_list: list):
    column_scores = []
    for column, feature in feature_list:
        column_scores.append({column: 0})
    
    return column_scores
    