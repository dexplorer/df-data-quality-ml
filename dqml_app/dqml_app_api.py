from dqml_app import settings as sc
from dqml_app import dqml_app_core as dqc
import logging

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    """
    Default route
    """

    return {"message": "Data Quality Machine Learning App"}


@app.get("/detect-anomalies/{dataset_id}")
async def detect_anomalies(dataset_id: str, env: str = "dev"):
    """
    Detect anomalies in the dataset.
    """

    cfg = sc.load_config(env)
    sc.set_config(cfg)

    # script_name = os.path.splitext(os.path.basename(__file__))[0]
    # ufl.config_logger(log_file_path_name=f"{sc.log_file_path}/{script_name}.log")
    logging.info("Configs are set")

    logging.info("Start detecting anomalies in the dataset %s", dataset_id)
    column_scores = dqc.detect_anomalies(dataset_id=dataset_id)

    logging.info("Finished detecting anomalies in the dataset %s", dataset_id)

    return {"results": column_scores}


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=8080,
        host="0.0.0.0",
        log_config=f"{sc.APP_ROOT_DIR}/cfg/dqml_app_api_log.ini",
        # reload=True,
    )
