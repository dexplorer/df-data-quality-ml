import pandas as pd
import numpy as np

# from shap import TreeExplainer
import shap
import matplotlib.pyplot as plt

from dqml_app import settings as sc


def get_shap_tree_explainer(model):
    explainer = shap.TreeExplainer(model)
    return explainer


def get_shap_values(explainer, data_for_prediction):
    shap_values = explainer.shap_values(data_for_prediction)
    return shap_values


def plot_shap_values(explainer, shap_values, data_for_prediction, dataset_id):
    # Summary plot for all data points
    fig1, ax1 = plt.subplots()
    ax1 = shap.summary_plot(
        shap_values, data_for_prediction, show=False, plot_type="bar"
    )
    summary_plot_file = f"{sc.plot_path}/dataset_id_{dataset_id}_shap_summary.png"
    plt.savefig(summary_plot_file, bbox_inches="tight")
    plt.clf()
    plt.close()

    # Force plot for a single data point
    # shap.initjs()
    # shap.force_plot(explainer.expected_value, shap_values, data_for_prediction)
    fig2, ax2 = plt.subplots()
    ax2 = shap.force_plot(
        explainer.expected_value,
        shap_values[0, :],
        data_for_prediction.iloc[0],
        show=False,
        matplotlib=True,
    )
    force_plot_file = f"{sc.plot_path}/dataset_id_{dataset_id}_shap_force.png"
    plt.savefig(force_plot_file, bbox_inches="tight")
    plt.clf()
    plt.close()

    # Waterfall plot for a single explanation
    fig3, ax3 = plt.subplots()
    explanation = explainer(data_for_prediction)
    # Print explanation object to see the values plotted in the waterfall plot
    # logging.debugexplanation)
    ax3 = shap.plots.waterfall(explanation[0], show=False)
    waterfall_plot_file = f"{sc.plot_path}/dataset_id_{dataset_id}_shap_waterfall.png"
    plt.savefig(waterfall_plot_file, bbox_inches="tight")
    plt.clf()
    plt.close()


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
    column_scores = shap_importance.to_dict("records")

    return column_scores
