import os
import argparse
import logging

from config.settings import ConfigParms as sc
from config import settings as scg
from dqml_app import dqml_app_core as dqc
from utils import logger as ufl

from fastapi import FastAPI
import uvicorn

#
APP_ROOT_DIR = "/workspaces/df-data-quality-ml"

app = FastAPI()


@app.get("/")
async def root():
    """
    Default route

    Args:
        none

    Returns:
        A default message.
    """

    return {"message": "Data Quality Machine Learning App"}


@app.get("/detect-anomalies/")
async def detect_anomalies(dataset_id: str, cycle_date: str = ""):
    """
    Detect anomalies in the dataset.

    Args:
        dataset_id: Id of the dataset.
        cycle_date: Cycle date

    Returns:
        Column/Feature scores that suggest an anomaly in the dataset.
    """

    logging.info("Started detecting anomalies in the dataset %s", dataset_id)
    column_scores = dqc.detect_anomalies(dataset_id=dataset_id, cycle_date=cycle_date)
    logging.info("Finished detecting anomalies in the dataset %s", dataset_id)

    return {"results": column_scores}


def main():
    parser = argparse.ArgumentParser(
        description="Data Quality Machine Learning Application"
    )
    parser.add_argument(
        "-e", "--env", help="Environment", const="dev", nargs="?", default="dev"
    )

    # Get the arguments
    args = vars(parser.parse_args())
    logging.info(args)
    env = args["env"]

    scg.APP_ROOT_DIR = APP_ROOT_DIR
    sc.load_config(env=env)

    script_name = os.path.splitext(os.path.basename(__file__))[0]
    ufl.config_logger(log_file_path_name=f"{sc.log_file_path}/{script_name}.log")
    logging.info("Configs are set")

    logging.info("Starting the API service")

    uvicorn.run(
        app,
        port=8080,
        host="0.0.0.0",
        log_config=f"{sc.cfg_file_path}/api_log.ini",
        # reload=True,
    )

    logging.info("Stopping the API service")


if __name__ == "__main__":
    main()
