import logging
import os

import click
from dqml_app import settings as sc
from dqml_app import dqml_app_core as dqc
from utils import logger as ufl


@click.command()
# @click.argument('dataset_id', required=1)
@click.option(
    "--dataset_id", type=str, default="dev", help="Source dataset id", required=True
)
@click.option("--env", type=str, default="dev", help="Environment")
@click.option("--cycle_date", type=str, default="", help="Cycle date")
def detect_anomalies(dataset_id: str, env: str, cycle_date: str):
    """
    Detect anomalies in the dataset.
    """

    sc.load_config(env)

    script_name = os.path.splitext(os.path.basename(__file__))[0]
    ufl.config_logger(log_file_path_name=f"{sc.log_file_path}/{script_name}.log")
    logging.info("Configs are set")

    logging.info("Started detecting anomalies in the dataset %s", dataset_id)
    column_scores = dqc.detect_anomalies(dataset_id=dataset_id, cycle_date=cycle_date)

    logging.info("Column/Feature scores for dataset %s", dataset_id)
    logging.info(column_scores)

    logging.info("Finished detecting anomalies in the dataset %s", dataset_id)


# Create command group
@click.group()
def cli():
    pass


# Add sub command to group
cli.add_command(detect_anomalies)


def main():
    cli()


if __name__ == "__main__":
    main()
