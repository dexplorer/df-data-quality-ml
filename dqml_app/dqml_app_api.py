from dqml_app import settings as sc
from dqml_app import dqml_app_core as dqc
from utils import logger as ufl
import logging
import os

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
    See ./log/dqml_app_cli.log for logs.
    """

    cfg = sc.load_config(env)
    sc.set_config(cfg)

    # script_name = os.path.splitext(os.path.basename(__file__))[0]
    # ufl.config_logger(log_file_path_name=f"{sc.log_file_path}/{script_name}.log")
    logging.info(f"Configs are set")

    logging.info(f"Start detecting anomalies in the dataset {dataset_id}")
    dq_results = dqc.detect_anomalies(dataset_id=dataset_id)

    logging.info(f"Finished detecting anomalies in the dataset {dataset_id}")

    return {"results": dq_results}


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=8080,
        host="0.0.0.0",
        log_config=f"{sc.APP_ROOT_DIR}/cfg/dqml_app_api_log.ini",
    )
