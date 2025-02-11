# import datetime as dt
from metadata import dataset as ds
from metadata import dataset_dq_model_parms as dqmp
from config.settings import ConfigParms as sc
from app_calendar import eff_date as ed
from utils import csv_io as ufc
from utils import spark_io as ufs
import random
import pandas as pd
import logging
import os


def query_random_sample(
    dataset: ds.LocalDelimFileDataset | ds.SparkTableDataset, dq_mdl_parm: dqmp.DatasetDQModelParameters, eff_date: str
) -> pd.DataFrame:
    # table: str, time_column: str, eff_date: dt.date, sample_size: int

    eff_date_yyyymmdd = ed.fmt_date_str_as_yyyymmdd(eff_date)

    src_data_records = []
    if dataset.kind == ds.DatasetKind.LOCAL_DELIM_FILE:
        # Read the source data file
        src_file_path = sc.resolve_app_path(
            dataset.resolve_file_path(eff_date_yyyymmdd)
        )

        if os.path.exists(src_file_path):
            logging.info("Reading the file %s", src_file_path)
            src_data_records = ufc.uf_read_delim_file_to_list_of_dict(
                file_path=src_file_path, delim=dataset.file_delim
            )
        else:
            logging.info("File %s does not exist. Skipping the file.", src_file_path)

    elif dataset.kind == ds.DatasetKind.SPARK_TABLE:
        # Read the spark table
        qual_target_table_name = dataset.get_qualified_table_name()
        logging.info("Reading the spark table %s", qual_target_table_name)
        src_data_records = ufs.read_spark_table_into_list_of_dict(
            qual_target_table_name=qual_target_table_name,
            cur_eff_date=eff_date,
            warehouse_path=sc.hive_warehouse_path,
        )

    sample_size = dq_mdl_parm.model_parameters.sample_size
    if sample_size < len(src_data_records):
        df = pd.DataFrame.from_dict(random.sample(src_data_records, sample_size))
    else:
        df = pd.DataFrame.from_dict(src_data_records)

    return df
