import logging
import os

import click
from dotenv import load_dotenv
from config.settings import ConfigParms as sc
from dqml_app import dqml_app_core as dqc
from utils import logger as ufl


# Create command group
@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--dataset_id", type=str, default="dev", help="Source dataset id", required=True
)
@click.option("--cycle_date", type=str, default="", help="Cycle date")
def detect_anomalies(dataset_id: str, cycle_date: str):
    """
    Detect anomalies in the dataset.
    """

    logging.info("Started detecting anomalies in the dataset %s", dataset_id)
    column_scores = dqc.detect_anomalies(dataset_id=dataset_id, cycle_date=cycle_date)

    logging.info("Column/Feature scores for dataset %s", dataset_id)
    logging.info(column_scores)

    logging.info("Finished detecting anomalies in the dataset %s", dataset_id)


def main():
    # Load the environment variables from .env file
    load_dotenv()

    # Fail if env variable is not set
    sc.load_config()

    script_name = os.path.splitext(os.path.basename(__file__))[0]
    ufl.config_logger(log_file_path_name=f"{sc.app_log_dir}/{script_name}.log")
    logging.info("Configs are set")
    logging.info(os.environ)
    logging.info(sc.config)
    logging.info(vars(sc))

    cli()


if __name__ == "__main__":
    main()
