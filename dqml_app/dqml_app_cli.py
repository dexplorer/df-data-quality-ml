import logging
import os

import click
from dqml_app import settings as sc
from dqml_app import dqml_app_core as dqc
from dqml_app.utils import logger as ufl


@click.command()
# @click.argument('dataset_id', required=1)
@click.option(
    "--dataset_id", type=str, default="dev", help="Source dataset id", required=True
)
@click.option("--env", type=str, default="dev", help="Environment")
def detect_anomalies(dataset_id: str, env: str):
    """
    Detect anomalies in the dataset.
    See ./log/dqml_app_cli.log for logs.
    """

    logging.info(f"Set configs")
    cfg = sc.load_config(env)
    sc.set_config(cfg)

    logging.info(f"Detecting anomalies in the dataset {dataset_id}")
    dq_check_results = dqc.detect_anomalies(dataset_id=dataset_id)

    click.echo(f"DQ check results for dataset {dataset_id}")
    click.echo(dq_check_results)

    logging.info(f"Finished applying DQ rules on the dataset {dataset_id}")


# Create command group
@click.group()
def cli():
    pass


# Add sub command to group
cli.add_command(detect_anomalies)


def main():
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    ufl.config_logger(log_file_name=script_name)
    cli()


if __name__ == "__main__":
    main()
