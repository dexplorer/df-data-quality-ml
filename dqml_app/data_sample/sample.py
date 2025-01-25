import datetime as dt
from metadata import dataset as ds
from dqml_app import settings as sc
from app_calendar import eff_date as ed
from utils import file_io as uff
import random
import pandas as pd
import logging


def query_random_sample(dataset: ds.Dataset, eff_date: str) -> pd.DataFrame:
    # table: str, time_column: str, eff_date: dt.date, sample_size: int

    eff_date_yyyymmdd = ed.fmt_date_str_as_yyyymmdd(eff_date)
    src_file_path = sc.resolve_app_path(dataset.resolve_file_path(eff_date_yyyymmdd))
    logging.debug("Reading the file {src_file_path}")
    src_file_records = uff.uf_read_delim_file_to_list_of_dict(file_path=src_file_path)

    sample_size = dataset.model_parameters.sample_size
    if sample_size < len(src_file_records):
        df = pd.DataFrame.from_dict(random.sample(src_file_records, sample_size))
    else:
        df = pd.DataFrame.from_dict(src_file_records)

    return df
