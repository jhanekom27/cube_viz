from pandas import DataFrame
import pandas as pd
from typing import Tuple

from cubeviz.models import TimiksData, CVBase
from cubeviz.config import cubeviz_config


class UploadFormats:
    TIMIKS = "timiks"


def parse_timiks_to_base(df: TimiksData) -> CVBase:
    df["solve_date_time"] = pd.to_datetime(df.date)
    df["time_sec"] = df.ms / 1000

    return df


def get_data_source_format(df: DataFrame):
    timiks_columns = ["id", "ms", "date", "puzzle"]
    data_columns = df.columns

    if all(col in data_columns for col in timiks_columns):
        return UploadFormats.TIMIKS
    else:
        raise Exception("Your data format could not be determined.")


def get_base_from_sample() -> Tuple[str, CVBase]:
    name = "sample.csv"
    data_path = cubeviz_config.default_data_path
    df_timiks_raw = pd.read_csv(data_path)
    df_base = parse_timiks_to_base(df_timiks_raw)
    return name, df_base
