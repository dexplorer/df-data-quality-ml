from dqml_app import settings as sc

import os
import argparse
import logging

from dqml_app import dqml_app_core as dqc
from dqml_app.utils import logger as ufl


def main():
    parser = argparse.ArgumentParser(description="Data Quality Validation ML Application")
    parser.add_argument(
        "-e", "--env", help="Environment", const="dev", nargs="?", default="dev"
    )
    parser.add_argument(
        "-d",
        "--dataset_id",
        help="Source data",
        const="1",
        nargs="?",
        default="1",
        required=True,
    )

    # Sample invocation
    # python dqml_app.py --env='dev' --dataset='2'

    logging.info(f"Starting {script_name}")

    # Get the arguments
    args = vars(parser.parse_args())
    logging.info(args)
    env = args["env"]
    src_dataset_id = args["dataset_id"]

    logging.info(f"Set configs")
    cfg = sc.load_config(env)
    sc.set_config(cfg)
    # print(sc.source_file_path)
    logging.info(cfg)

    dq_check_results = dqc.detect_anomalies(dataset_id=src_dataset_id)

    print(f"DQ check results for dataset {src_dataset_id}")
    print(dq_check_results)

    logging.info(f"Finishing {script_name}")


if __name__ == "__main__":
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    ufl.config_logger(log_file_name=script_name)
    main()
